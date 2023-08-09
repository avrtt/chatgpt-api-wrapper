from pydantic.v1 import BaseSettings
from dotenv import load_dotenv

# .env file
load_dotenv()


class Settings(BaseSettings):
    """
    Config
    """
    VERBOSE: bool = False
    OPENAI_API_KEY: str | None = None
    
    TEMPLATE_PATH: str = 'chatgpt_api_wrapper/prompts'
    TEMPLATE_EXT: str = '.template'
    

settings = Settings()
