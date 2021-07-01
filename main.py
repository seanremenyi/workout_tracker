import requests
from datetime import datetime

GENDER = "male"
WEIGHT_KG = 99
HEIGHT_CM = 180
AGE = 30


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

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = ""

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

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)
    print(sheet_response.text)
