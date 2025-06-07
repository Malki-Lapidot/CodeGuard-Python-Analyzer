from pymongo import MongoClient
from datetime import datetime

# התחברות למסד הנתונים
client = MongoClient("mongodb://localhost:27017")
db = client["project_db"]                # שם הדאטהבייס
collection = db["versions"]             # שם הקולקשן

# פונקציה לשמירת גרסה
def save_version(issue_count: int):
    version_data = {
        "date": datetime.now(),         # תאריך ושעה נוכחיים
        "issue_count": issue_count      # כמות בעיות שנמצאו בגרסה
    }
    collection.insert_one(version_data)
    print("✅ גרסה נשמרה:", version_data)
