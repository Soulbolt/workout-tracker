import os
from dotenv import load_dotenv
import requests
from datetime import datetime

load_dotenv()

# Require secrets for API service authentication
APP_ID = os.getenv("Nutritionix_APP_ID")
API_KEY = os.getenv("Nutritionix_API_KEY")
SHEETY_USERNAME = os.getenv("SHEETY_USERNAME")
BASIC_AUTH = os.getenv("BASIC_AUTH")

# API call to Natural Language for Exercise
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {
    "Content-Type" : "application/json",
    "x-app-id" : APP_ID,
    "x-app-key" : API_KEY,
}

# Date and format to API call requirement
today = datetime.now()
formmatted_date = today.strftime("%d/%m/%Y")

# Get input for Query exercise event
query = {
    "query" : input("What exercise did you perform? \n")
    }

# API call to get excerise data
response = requests.post(url=NUTRITIONIX_ENDPOINT, headers=headers, json=query)
data = response.json()
exercise_data = data["exercises"]

# Sheety API call to post exercise data event to google sheets doc
GOOGLE_DOC_ENDPOINT = f"https://api.sheety.co/{SHEETY_USERNAME}/myWorkouts/workouts"
AUTH_PARAMS = {
    "Authorization" : BASIC_AUTH,
}

# For loop to iterate if there is more than 1 exercise and post eaech one through the Sheety API call with the extracted data.
for index in range(len(exercise_data)):
    exercise_report = {}
    if "name" in exercise_data[index]:        
        exercise_report = {
            "workout" : {
            "date" : formmatted_date,
            "time" : today.strftime("%X"),
            "exercise": exercise_data[index]["name"].title(),
            "duration": exercise_data[index]["duration_min"],
            "calories": exercise_data[index]["nf_calories"],
            }
        }
    post_to_google_doc = requests.post(url=GOOGLE_DOC_ENDPOINT, json=exercise_report, headers=AUTH_PARAMS)
    print(post_to_google_doc.json())

# Delete Entry using Sheety API call for Google Sheets doc usind id(row number)
# response = requests.delete(url=GOOGLE_DOC_ENDPOINT+"/3")
# print(response.text)
