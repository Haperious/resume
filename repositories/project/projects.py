from pymongo import ASCENDING
from bson import ObjectId
from datetime import datetime
from flask import current_app


class ProjectsRepo:
    def __init__(self):
        self.collection = current_app.db["my_resume"]["projects"]
        if self.collection is None:
            raise ValueError("MongoDB collection 'projects' is not initialized.")

    def get_projects(self):

       
        try:
            projects = list(
                self.collection.find({}, {"_id": 0}).sort("id", 1)
            )

            if projects:
                return projects

            else:
                return None
            # return data if data else None
        except Exception as e:

            return {"error": str(e), "message": "Failed to Retrieve User."}
