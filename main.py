import requests
from datetime import datetime
import os

API_ID = os.environ["API_ID"]
API_KEY = os.environ["API_KEY"]
GENDER = Your Gender
WEIGHT_KG = Your Weight
HEIGHT_CM = Your Height
AGE = Your age

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = os.environ["sheet_endpoint"]

text = input("what exercise did you today")

user_params = {
 "query": text,
 "gender": GENDER,
 "weight_kg": WEIGHT_KG,
 "height_cm": HEIGHT_CM,
 "age": AGE
}

headers = {
 "x-app-id": API_ID,
 "x-app-key": API_KEY,
 "Content-Type": "application/json"
}

response = requests.post(url=exercise_endpoint, json=user_params, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    bearer_headers = {
     "Authorization": f"Bearer {os.environ['token']}"
    }
    sheet_response = requests.post(
     sheet_endpoint,
     json=sheet_inputs,
     headers=bearer_headers
    )

    print(sheet_response.text)
