import os
from datetime import timedelta
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class Config:
    """Flask application configuration."""

    SECRET_KEY = os.getenv("SECRET_KEY")

    # MongoDB URIs for different databases
    MONGO_URIS = {
        "main": os.getenv("MONGO_AI"),
        
    }

    # # Flask-Session Configurations
    # SESSION_TYPE = "mongodb"
    # SESSION_PERMANENT = True
    # SESSION_USE_SIGNER = True
    # PERMANENT_SESSION_LIFETIME = timedelta(hours=1)
