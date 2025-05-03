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

# This will now work with single-line text
for i in range(10):  # test with 10 rows first
    data = {
        "fields": {
            "ID": f"{i+1:04}",
            "Platform": "Facebook",  # this is a plain string
            "Time": "",
            "Content Type": "",
            "Post Content": [],
            "Status": "Draft",
            "Link": [],
            "Trend": "",
        }
    }

    url = f"https://api.airtable.com/v0/{BASE_ID}/{TABLE_NAME}"
    response = requests.post(url, json=data, headers=headers)

    if response.status_code != 200:
        print(f"Error at row {i+1}: {response.text}")
