import os
import requests
from dotenv import load_dotenv
import random

load_dotenv()

API_TOKEN = os.getenv("AIRTABLE_TOKEN")
BASE_ID = os.getenv("BASE_ID")
TABLE_NAME = os.getenv("TABLE_NAME")

headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

# List of platforms (updated with the valid options in your Airtable)
Platform = ["Medium", "Blog", "Facebook", "Instagram", "TikTok", "Lemon8"]

# Example of 728 blank rows (customize this block as needed)
for i in range(728):
    Platform = random.choice(Platform)  # Randomly choose a platform for each row
    
    data = {
        "fields": {
            "ID": f"{i+1:04}",  # Automatically generates ID with leading zeros
            "Platform": {"name": Platform},  # Use the random platform for the row
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
