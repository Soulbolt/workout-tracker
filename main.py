import os
from dotenv import load_dotenv
import requests
from datetime import datetime

load_dotenv()

APP_ID = os.getenv("Nutritionix_APP_ID")
API_KEY = os.getenv("Nutritionix_API_KEY")
SHEETY_USERNAME = os.getenv("SHEETY_USERNAME")

NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {
    "Content-Type" : "application/json",
    "x-app-id" : APP_ID,
    "x-app-key" : API_KEY,
}

today = datetime.now()
# formmatted_date = today.strftime("%d/%m/%Y")

# query = {
#     "query" : input("What exercise did you perform? \n")
#     }
# response = requests.post(url=NUTRITIONIX_ENDPOINT, headers=headers, json=query)
# data = response.json()
# exercise_data = data["exercises"]

GOOGLE_DOC_ENDPOINT = f"https://api.sheety.co/{SHEETY_USERNAME}/myWorkouts/workouts"
# for index in range(len(exercise_data)):
#     exercise_report = {}
#     if "name" in exercise_data[index]:        
#         exercise_report = {
#             "workout" : {
#             "date" : formmatted_date,
#             "time" : today.strftime("%X"),
#             "exercise": exercise_data[index]["name"].title(),
#             "duration": exercise_data[index]["duration_min"],
#             "calories": exercise_data[index]["nf_calories"],
#             }
#         }
#     post_to_google_doc = requests.post(url=GOOGLE_DOC_ENDPOINT, json=exercise_report)
#     print(post_to_google_doc.json())

response = requests.delete(url=GOOGLE_DOC_ENDPOINT+"/3")
print(response.text)
