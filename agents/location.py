# agents/location.py
from google.adk.agents import Agent
from google.adk.models import Gemini
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from config.settings import settings
from google.adk.tools import google_search
import asyncio
import json


class LocationAgent:
    """Wrapper for the Location ADK agent."""
    
    def __init__(self):
        """Initialize the location agent."""
        self.agent = Agent(
            name="LocationAgent",
            model=Gemini(
                model=settings.DEFAULT_MODEL,
            ),
            description="An agent that takes a zip code, finds the assigned residential recycling store, provides recycling regulations and accepted RIC codes for that store.",
            instruction="""
**CRITICAL: You must respond with ONLY valid JSON. No markdown, no explanations, no additional text before or after the JSON.**

Your task:
1. Receive a zip code from the user
2. Search for the assigned residential recycling store for that zip code
3. Retrieve recycling regulations and accepted RIC codes for that store
4. Return ONLY the JSON response (no markdown code blocks, no text)

**If the zip code is invalid, return ONLY this JSON:**
{"success": false, "error": "Reason it failed"}

**If successful, return ONLY this JSON structure:**
{
  "zip_code": "zipcode of the user",
  "municipality": "municipality of that zipcode",
  "state": "which state does this zipcode belong to",
  "local_authority": {
    "name": "name of the assigned residential recycle store",
    "website": "website of the assigned residential recycle store",
    "phone": "phone number of the assigned residential recycle store"
  },
  "curbside_recycling": {
    "accepts": ["RIC code 1", "RIC code 2"],
    "rejects": ["RIC code 3", "RIC code 4"],
    "special_instructions": "Any special instructions for recycling"
  },
  "confidence": 0.85
}

Rules:
- DO NOT use markdown code blocks (no ```json or ```)
- DO NOT add any explanatory text before or after the JSON
- Confidence must be a number between 0 and 1 (e.g., 0.85, not "0.85")
- If you cannot find complete information, fill in what you can and set confidence lower
- Only respond in English
- Only answer questions about recycling stores, regulations, or RIC codes
""",
            tools=[google_search]
        )
        
        # Create session service and runner
        self.session_service = InMemorySessionService()
        self.runner = Runner(
            agent=self.agent,
            app_name="agents",
            session_service=self.session_service
        )
        
        self.USER_ID = "user_location"
        self.SESSION_ID = "session_location"

        # Create session immediately during initialization (async call)
        asyncio.run(self.session_service.create_session(
            app_name="agents",
            user_id=self.USER_ID,
            session_id=self.SESSION_ID
        ))

        print(f"✅ LocationAgent initialized")
    
    def run(self, zip_code: str, debug: bool = False):
        """
        Run location lookup synchronously.
        
        Args:
            zip_code: 5-digit US zip code
            debug: Whether to use debug mode
            
        Returns:
            Parsed JSON response
        """
        print(f"🔍 LocationAgent.run() called with zip_code: {zip_code}")
        
        # Run the async execute method synchronously
        try:
            result = asyncio.run(self._execute(zip_code))
            return result
        except RuntimeError:
            # Event loop already running in Streamlit
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            try:
                result = loop.run_until_complete(self._execute(zip_code))
                return result
            finally:
                loop.close()
    
    async def _execute(self, zip_code: str):
        """Internal async execution method."""
        # Session was already created in __init__

        # Create prompt
        prompt = f"Find recycling information for zip code: {zip_code}"
        
        # Create message
        message = types.Content(role="user", parts=[types.Part(text=prompt)])
        
        # Run agent and collect response
        async for event in self.runner.run_async(
            user_id=self.USER_ID,
            session_id=self.SESSION_ID,
            new_message=message
        ):
            if event.is_final_response():
                response_text = event.content.parts[0].text
                
                # Try to parse as JSON
                try:
                    # Remove markdown code blocks if present
                    if '```json' in response_text or '```' in response_text:
                        response_text = response_text.replace('```json', '').replace('```', '').strip()
                    
                    parsed = json.loads(response_text)
                    return parsed
                except json.JSONDecodeError as e:
                    print(f"❌ JSON parsing failed: {e}")
                    print(f"Response content: {response_text}")
                    return {
                        "success": False,
                        "error": "Failed to parse response",
                        "raw_response": response_text
                    }
        
        # If we get here, no final response was received
        return {
            "success": False,
            "error": "No response received from agent"
        }