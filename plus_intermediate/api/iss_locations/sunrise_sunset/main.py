import requests
from datetime import datetime

LAT = 43.792780
LNG = -79.413190

parameters = {
    "lat": LAT,
    "lng": LNG,
    "formatted":0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)

response.raise_for_status()

data = response.json()

sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

sunrise_hr = sunrise.split("T")[1].split(":")[0]
sunset_hr = sunset.split("T")[1].split(":")[0]

time_now = datetime.now()

print(sunrise_hr, sunset_hr)
print(time_now.hour)