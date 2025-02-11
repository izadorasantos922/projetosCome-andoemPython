import datetime as dt
import pandas
import random
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()
MY_EMAIL = os.getenv("EMAIL")
MY_PASSWORD = os.getenv("PASSWORD")

random_letter = f"letter_1.txt"

now = dt.datetime.now()
month_day = (now.month, now.day)

data = pandas.read_csv("birth.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if month_day in birthdays_dict:
    birthday_person = birthdays_dict[month_day]

    with open(f"./letter_templates/{random_letter}", "r") as file:
        letter_data = file.read()
        personalized_letter = letter_data.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject: Happy Birthday!\n\n{personalized_letter}"
        )

    print("E-mail enviado com sucesso!")
else:
    print("Hoje não é aniversário de ninguém.")
