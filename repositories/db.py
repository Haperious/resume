from pymongo import MongoClient, errors
from pymongo.server_api import ServerApi
from flask import current_app, g


class DatabaseManager:
    """Handles multiple MongoDB connections and ensures they remain open."""

    _instance = None  # Singleton pattern to prevent multiple initializations

    def __new__(cls, mongo_uris):
        """Ensures that only one instance of DatabaseManager exists."""
        if cls._instance is None:
            cls._instance = super(DatabaseManager, cls).__new__(cls)
            cls._instance.clients = {}
            for name, uri in mongo_uris.items():
                cls._instance.clients[name] = cls._instance._init_mongo_client(
                    name, uri
                )
                if cls._instance.clients[name]:
                    print(
                        f"{name.capitalize()} MongoDB connection established successfully."
                    )
        return cls._instance

    def _init_mongo_client(self, name, uri):
        """Initializes a MongoDB client and prevents premature closure."""
        try:
            client = MongoClient(
                uri, server_api=ServerApi("1"), tlsAllowInvalidCertificates=True
            )

            client.server_info()  # Test connection
            return client
        except errors.ServerSelectionTimeoutError as e:
            print(f"Error connecting to {name.capitalize()} MongoDB: {e}")
            return None

    def get_database(self, client_name, db_name):
        """Fetches a specific database from a given client."""
        client = self.clients.get(client_name)
        if client is None:
            raise ValueError(f"MongoDB client '{client_name}' is not available.")
        return client[db_name] if db_name in client.list_database_names() else None

    def close_connections(self):
        """Closes MongoDB connections ONLY when shutting down the app."""
        for name, client in self.clients.items():
            if client:
                client.close()
                print(f"Closed {name.capitalize()} MongoDB connection.")


# Initialize MongoDB connection when the app starts
def init_db(app, config):
    """Ensure MongoDB connections persist throughout the app lifecycle."""
    db_manager = DatabaseManager(config.MONGO_URIS)

    # Assign MongoDB collections
    app.db = {
        "amadeus-helpdesk-ai": db_manager.get_database("main", "amadeus-helpdesk-ai"),
    }

    app.ms_customers = {
        "morningstars": db_manager.get_database("secondary", "morningstars")
    }

    # # Configure Flask-Session
    # app.config["SESSION_MONGODB"] = db_manager.clients["main"]
    # app.config["SESSION_MONGODB_DB"] = "joury_travels"
    # app.config["SESSION_MONGODB_COLLECTION"] = "sessions"

    # # Close MongoDB connections ONLY when Flask shuts down
    # @app.teardown_appcontext
    # def close_db_connection(exception=None):
    #     print("Teardown event triggered, but MongoDB connections remain open.")

    # @app.teardown_appcontext
    # def teardown_repositories(exception=None):
    #     """Clean up repositories to avoid persistence across requests."""
    #     g.pop("customer_repo", None)
    #     g.pop("agreement_repo", None)
    #     g.pop("office_repo", None)
    #     g.pop("unpaid_airline_repo", None)
    #     g.pop("incentive_repo", None)
    #     g.pop("user_selco_repo", None)
    #     g.pop("user_repo", None)
