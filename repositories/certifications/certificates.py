from pymongo import ASCENDING
from bson import ObjectId
from datetime import datetime
from flask import current_app


class CertificatesRepo:
    def __init__(self):
        self.collection = current_app.db["my_resume"]["certificates"]
        if self.collection is None:
            raise ValueError("MongoDB collection 'certificates' is not initialized.")

    def get_certificates(self):

       
        try:
            certificates = list(
                self.collection.find({}, {"_id": 0}).sort("type", 1)
            )

            if certificates:
                return certificates

            else:
                return None
            # return data if data else None
        except Exception as e:

            return {"error": str(e), "message": "Failed to Retrieve User."}
