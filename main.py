import requests
from twilio.rest import Client
import os


API_KEY = os.environ.get("OWM_API_KEY")
API_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
MY_PHONE_NUMBER = os.environ.get("MY_PHONE_NUMBER")
TWILIO_PHONE = os.environ.get("TWILIO_PHONE")

parameters = {
    "lat": 51.160522,
    "lon": 71.470360,
    "appid": API_KEY,
    "cnt": 4
}


response = requests.get(url=API_ENDPOINT, params=parameters)
response.raise_for_status()

weather_data = response.json()
print(weather_data)




weather_list = weather_data["list"]
print(weather_list)

codes = []

for three_hour_period in weather_list:
       for condition in three_hour_period["weather"]:
           codes.append(condition["id"])

print(f"codes: {codes}")

is_rainy_today = False

for code in codes:
    if code < 700:
        is_rainy_today = True

if is_rainy_today:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Don't forget an umbrella",
        from_=f"whatsapp:{TWILIO_PHONE}",
        to=f"whatsapp:{MY_PHONE_NUMBER}",
    )

    print(message.status)





