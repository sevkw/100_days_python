import requests
from datetime import datetime
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv(".env.pixela")
PIXELA_USERNAME = os.getenv("PIXELA_USERNAME")
PIXELA_TOKEN =  os.getenv("PIXELA_TOKEN")

pixela_endpoint = "https://pixe.la/v1/users"

GRAPH_ID = "gymtracker2307"

user_params = {
    "token": PIXELA_TOKEN,
    "username": PIXELA_USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

graph_config = {
    "id": GRAPH_ID,
    "name": "Gym Exercise Graph",
    "unit": "minutes",
    "type": "int",
    "color": "ajisai"
}

pixela_headers = {
    "X-USER-TOKEN": PIXELA_TOKEN
}
# /v1/users/<username>/graphs
graph_endpoint = f"{pixela_endpoint}/{PIXELA_USERNAME}/graphs"

## Adding a new graph
# response = requests.post(url=graph_endpoint, json=graph_config, headers=pixela_headers)

## Add a pixel
#/v1/users/<username>/graphs/<graphID>
pixel_endpoint = f"{pixela_endpoint}/{PIXELA_USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

graph_pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many minutes did you exercise today?: ")
}

# add a pixel for the specified date
# response = requests.post(url=pixel_endpoint, json=graph_pixel_config, headers=pixela_headers)
# print(response.text)
## can validate the pixel at here: https://pixe.la/v1/users/kerrywang/graphs/gymtracker2307.html


## UPDATE PIXEL

#/v1/users/<username>/graphs/<graphID>/<yyyyMMdd>
date_to_update = datetime(2023, 7, 6).strftime("%Y%m%d")
update_pixel_endpoint = f"{pixela_endpoint}/{PIXELA_USERNAME}/graphs/{GRAPH_ID}/{date_to_update}"
update_config = {
    "quantity": "92"
}

# response = requests.put(url=update_pixel_endpoint, json=update_config, headers=pixela_headers)
# print(response.text)

## DELETE A PIXEL
#/v1/users/<username>/graphs/<graphID>/<yyyyMMdd>
delete_endpoint = update_pixel_endpoint
# response = requests.delete(url=delete_endpoint, headers=pixela_headers)
# print(response.text)