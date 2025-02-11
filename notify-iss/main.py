import requests 
from datetime import datetime
from time import sleep
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()
MY_EMAIL = os.getenv("EMAIL")
MY_PASSWORD = os.getenv("PASSWORD")
to_email = "isadorasantosdesousa948@gmail.com"
lat = -4.447860
long = -49.111301

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_lat = float(data["iss_position"]["latitude"])
iss_long = float(data["iss_position"]["longitude"])

def within_lat_long():
    return lat-5 <= iss_lat <= lat+5 and long-5 <=iss_long <= long+5 <= iss_long

parameters = {
    "lat": lat,
    "lng": long,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
time_now = datetime.now()

while True:
    if time_now.hour >= sunset and within_lat_long():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendemail(from_addr=MY_EMAIL, to_addrs=to_email, msg="Subject: International Space Station Alert\n\nLook into the sky, you can see the ISS passing")
    sleep(60)
