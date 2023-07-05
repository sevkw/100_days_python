import requests
## Twilio documentation: https://www.twilio.com/docs/sms/quickstart/python
import os
# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
## the following import needed if running on PythonAnywhere
## https://help.pythonanywhere.com/pages/TwilioBehindTheProxy/
from twilio.http.http_client import TwilioHttpClient

api_key = 'b10f8b817e78e67523ac8fbae4f910a4'

one_call_url = 'https://api.openweathermap.org/data/3.0/onecall'

one_call_param = {
    "lat": 43.759840,
    "lon": -79.411210,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

TWILIO_ACCOUNT_SID = ""
TWILIO_AUTH_TOKEN = ""
TWILIO_PHONE_NUM = ""
TO_PHONE_NUM = ""


response = requests.get(one_call_url, params=one_call_param)
response.raise_for_status
print(response.status_code)

account_sid = os.environ[TWILIO_ACCOUNT_SID]
auth_token = os.environ[TWILIO_AUTH_TOKEN]


# using list comprehension
weather_data = response.json()["hourly"][:12]
condition_list = [int(i) for i in weather_data["weather"][0]["id"] if int(i) < 700]
if len(condition_list) > 0:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
                .create(
                     body="Bring an Umbrella",
                     from_=TWILIO_PHONE_NUM,
                     to=TO_PHONE_NUM
                 )
    
    print(message.sid)
    print(message.status)

## Angela's code
# will_rain = False

# for hour_data in weather_data:
#     condition_code = hour_data["weather"][0]["id"]
#     if int(condition_code) < 700:
#         will_rain = True

# if will_rain:
#     print("Bring an Umbrella")