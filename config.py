import os
from datetime import timedelta
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class Config:
    """Flask application configuration."""

    # SECRET_KEY = os.getenv("SECRET_KEY")

    # MongoDB URIs for different databases
    MONGO_DB = {
        "main": os.getenv("MONGO_DB"),
        
    }

    # # Flask-Session Configurations
    # SESSION_TYPE = "mongodb"
    # SESSION_PERMANENT = True
    # SESSION_USE_SIGNER = True
    # PERMANENT_SESSION_LIFETIME = timedelta(hours=1)
