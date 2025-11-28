import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # API Keys
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    
    # Model Configuration
    DEFAULT_MODEL = "gemini-2.5-flash-lite"
    
    # Agent Settings
    MAX_RETRIES = 3
    TIMEOUT_SECONDS = 30
    
    # Feature Flags
    DEBUG_MODE = os.getenv("DEBUG_MODE", "false").lower() == "true"

settings = Settings()
