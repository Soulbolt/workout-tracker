import os
from dotenv import load_dotenv
import requests

load_dotenv()

APP_ID = os.getenv("Nutritionix_APP_ID")
API_KEY = os.getenv("Nutritionix_API_KEY")

NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {
    "Content-Type" : "application/json",
    "x-app-id" : APP_ID,
    "x-app-key" : API_KEY,
    # "x-remote-user-id": "0",
}

query = {
    "query" : input("What exccise did you perform? \n")
    }
response = requests.post(url=NUTRITIONIX_ENDPOINT, headers=headers, json=query)

print(response.text)