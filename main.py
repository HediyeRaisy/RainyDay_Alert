import requests
import os
from twilio.rest import Client
account_sid = os.environ["ACCOUNT"]
key = os.environ["KEY"]
p = {
    "lat" : "35.6892523",
    "lon" : "51.3896004",
    "appid" : os.environ["APPID"],

}
response = requests.get("https://api.openweathermap.org/data/2.5/onecall",params= p)
for i in range (6,19):
    if response.json()['hourly'][i]['weather'][0]["id"] < 700:
        print("Bring Umbrella with yourself")
        client = Client(account_sid, key)

        message = client.messages \
            .create(
            body="Today is Rainy.\nDon't forget to bring an umbrella with yourself☔",
            from_=os.environ["NUM1"],
            to=os.environ["NUM2"]
        )

        print(message.sid)
        break




