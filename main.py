import requests


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

response = requests.post(url=exercise_endpoint, json=user_params, headers=headers)

print(response.json())