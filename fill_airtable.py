import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("AIRTABLE_TOKEN")
BASE_ID = os.getenv("BASE_ID")
TABLE_NAME = os.getenv("TABLE_NAME")

headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

# Example of 728 blank rows (customize this block as needed)
for i in range(728):
    data = {
        "fields": {
            "ID": f"{i+1:04}",
            "Platform": "Facebook",
            "Time": "",
            "Content Type": "Image",
            "Post Content": "",
            "Publish Date": "",
            "Status": "Draft",
            "Link": "",
            "Tags": [],
            "Notes": "",
            "Engagement": "",
            "Trend": "",
            "Content title": ""
        }
    }

    response = requests.post(
        f"https://api.airtable.com/v0/{BASE_ID}/{TABLE_NAME}",
        json=data,
        headers=headers
    )

    if response.status_code != 200:
        print(f"Error at row {i+1}: {response.text}")
