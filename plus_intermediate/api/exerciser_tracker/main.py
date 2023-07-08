import os
from dotenv import load_dotenv
import requests
from datetime import datetime, date

load_dotenv(".env.ex_tracker")

APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")

GENDER = os.getenv("GENDER")
WEIGHT_KG = os.getenv("WEIGHT_KG")
HEIGHT = os.getenv("HEIGHT")
AGE = os.getenv("AGE")

BEARER_TOKEN = os.getenv("BEARER_TOKEN")

### Nutritionix Doc: https://docs.google.com/document/d/1_q-K-ObMTZvO0qUEAxROrN3bwMujwAN25sLHwJzliK0/edit#
## Live demo for dev validation: https://www.nutritionix.com/natural-demo/exercise?q=ran%2010%20mins

## Nutritionix API Code from: 
## https://gist.github.com/mattsilv/d99cd145cc2d44d71fa5d15dd4829e03?permalink_comment_id=4327567#gistcomment-4327567

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_input = input("Tell me which exercise you did today?: ")

header = {
    "x-app-id": APP_ID,
    'x-app-key': API_KEY
}

parameters = {
    'query': exercise_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT,
    "age": AGE,
}

exercise_response = requests.post(url=exercise_endpoint, json=parameters, headers=header)
exercise_response.raise_for_status()
result = exercise_response.json()
exercises = result["exercises"]

## {'workouts': [{'date': '21/07/2020', 'time': '15:00:00', 'exercise': 'Running', 'duration': 22, 'calories': 130, 'id': 2}]}
for exercise in exercises:
    exercise_contents = {
        'workout':
        {
            'date': datetime.now().strftime("%d/%m/%Y"),
            'time': datetime.now().strftime("%X"),
            'exercise': exercise['name'].title(), 
            'duration': exercise['duration_min'],
            'calories': exercise['nf_calories'],
            } 
    }
# print(exercise_contents)
    sheety_endpoint = os.getenv("SHEETY_ENDPOINT")

    sheety_header = {
        "Authorization": BEARER_TOKEN,
    }

    ## POST API

    update_sheet_response = requests.post(url=sheety_endpoint, headers=sheety_header, json=exercise_contents)
    print(update_sheet_response)
    print(update_sheet_response.json())

# Get API
# sheety_response = requests.get(url=sheety_endpoint, headers=sheety_header)

# print(sheety_response.json())

# print(sheety_endpoint)

