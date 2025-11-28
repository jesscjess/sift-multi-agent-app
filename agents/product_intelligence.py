from google.adk import Agent
from google.adk.models import Gemini
from google.adk.runners import InMemoryRunner
from config.settings import settings
from google.adk.tools import google_search
import asyncio
import nest_asyncio

nest_asyncio.apply()


class ProductIntelligenceAgent:
    """Wrapper for the Product Intelligence ADK agent."""
    
    def __init__(self):
        agent = Agent(
            name="ProductIntelligenceAgent",
            model=Gemini(
                model=settings.DEFAULT_MODEL,
            ),
            description="Provides recycling information for products by searching the internet and returns results in a structured JSON format. Categorizes product_category into beverage_container, food_container, bottle, cup, bag, packaging, or other. Ensures confidence value is between 0 and 1. If information is unavailable, returns 'NA' for all fields.",
            instruction="""
            - **CRITICAL**: Before searching, check if the input is a specific, branded product name (e.g., "Coca-Cola Can"). If the input is a generic name (e.g., "glass bottle", "plastic cup", "shampoo bottle", "lotion") or likely non-existent, immediately return the 'failed' JSON format.
            - Accept product name as input from the user.
            - Search the internet for recycling information related to the provided product name.
            - it should respond in this JSON format:
            {
            "product_name": "The product name given by user",
            "brand": "Brand name of product",
            "ric_code": "the ric code for the recycling product ",
            "material_name": "what kind of material is the product container made of ex: Polystyrene ",
            "confidence": "ability to properly sort and recycle an item range should be between 0 and 1 ex: 0.89",
            "product_category": "what kind of container is it. ex : beverage_container, food_container, bottle, cup, bag, packaging, other",
            "notes": "recycling summary for product"
            }
            - if it cannot find product related data OR if the input was a generic product name as described above, then respond in this JSON format ONLY:
            {
            "success": False,
            "error": "Reason it failed"
            }
            - Ensure the confidence value in the response JSON is always between 0 and 1.
            - If recycling information cannot be found for the specific product after searching, respond with a JSON output where all values are 'N/A' (only for the successful format).
            - Ensure clear and concise communication with the user.
            - Handle user queries efficiently and provide accurate information.
            - Maintain a helpful and informative tone throughout interactions.
            """,
            tools=[google_search]
        )
        self.runner = InMemoryRunner(agent=agent)
    
    def run(self, product_name: str, debug: bool = False):
        """
        Run product analysis synchronously.
        
        Args:
            product_name: Name or description of the product
            debug: Whether to use debug mode
            
        Returns:
            Agent response
        """
        import asyncio
        
        # Create new event loop for sync context
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
        try:
            if debug:
                result = loop.run_until_complete(self.runner.run_debug(product_name))
            else:
                result = loop.run_until_complete(self.runner.run(product_name))
            return result
        finally:
            loop.close()