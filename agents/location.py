from google.adk import Agent
from google.adk.models import Gemini
from google.adk.runners import InMemoryRunner
from config.settings import settings
from google.adk.tools import google_search
import asyncio
import nest_asyncio

nest_asyncio.apply()

class LocationAgent:
    """Wrapper for the Location ADK agent."""
    
    def __init__(self):
        agent = Agent(
            name="LocationAgent",
            model=Gemini(
                model=settings.DEFAULT_MODEL,
            ),
            description="An agent that takes a zip code, finds the assigned residential recycling store, provides recycling regulations and accepted RIC codes for that store, and if regulations cannot be retrieved, supplies the store's website URL. All responses are formatted in a specific JSON structure with detailed fields for zip code, municipality, state, local authority info, curbside recycling details, and confidence score.",
            instruction="""
            - Receive a zip code from the user.
            -- If the zip code is not valid, respond with JSON format:
            {
            "success": false,
            "error": "Reason it failed"
            }
            - Search for the assigned residential recycling store for the provided zip code location.
            - Retrieve and provide recycling regulations and accepted RIC codes specific to that residential recycling store 
            - it should respond in this JSON format:
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
                "accepts": [
                "accepted RIC codes specific to that residential recycling store"
                ],
                "rejects": [
                "not accepted RIC codes specific to that residential recycling store"
                ],
                "special_instructions": {
                "Any special instructions for recycling for that residential recycling store"
                }
            },
            "confidence": "it shows how accurate the system is about the information it should range between 0 to 1"
            }
            - If recycling regulations information cannot be fetched, respond with the URL of the recycling store's website and fill other fields as best as possible.
            - Communicate clearly and concisely, ensuring the user receives accurate and relevant information for their location.
            - Do not repeat information already provided in previous responses.
            - Only respond in English.
            - Do not answer questions unrelated to recycling stores, regulations, or RIC codes.
            """,
            tools=[google_search]
        )
        self.runner = InMemoryRunner(agent=agent)
    
    def run(self, zip_code: str, debug: bool = False):
        """
        Run location lookup synchronously.
        
        Args:
            zip_code: 5-digit US zip code
            debug: Whether to use debug mode
            
        Returns:
            Agent response
        """
        # Create a new runner for each request
        runner = InMemoryRunner(agent=self.agent)
        
        try:
            if debug:
                result = asyncio.run(runner.run_debug(zip_code))
            else:
                result = asyncio.run(runner.run(zip_code))
            return result
        except RuntimeError:
            # Event loop already running in Streamlit
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            try:
                if debug:
                    result = loop.run_until_complete(runner.run_debug(zip_code))
                else:
                    result = loop.run_until_complete(runner.run(zip_code))
                return result
            finally:
                loop.close()