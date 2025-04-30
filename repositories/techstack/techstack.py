from pymongo import ASCENDING
from bson import ObjectId
from datetime import datetime
from flask import current_app


class TechStackRepo:
    def __init__(self):
        self.collection = current_app.db["my_resume"]["tech_stack"]
        if self.collection is None:
            raise ValueError("MongoDB collection 'tech_stack' is not initialized.")

    def get_techstack(self):

       
        try:
            tech_stack = list(
                self.collection.find({}, {"_id": 0}).sort("id", 1)
            )

            if tech_stack:
                return tech_stack

            else:
                return None
            # return data if data else None
        except Exception as e:

            return {"error": str(e), "message": "Failed to Retrieve User."}
