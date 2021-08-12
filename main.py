import smtplib as mail
import datetime as dt
import pandas
import random
import os

PLACEHOLDER = "[NAME]"

my_email = "testjerryc@gmail.com"
pw = "1pass2word_"

today = dt.datetime.now().date()
month = today.month
day = today.day

birthdays = pandas.read_csv("birthdays.csv").to_dict(orient="records")
birthday_names = [name for name in birthdays if name["month"] == month and name["day"] == day]


def birthday_wish():
    if birthday_names:
        for record in birthday_names:
            name = record["name"]
            letter = "./letter_templates/" + random.choice(os.listdir("letter_templates"))
            with open(letter) as letter:
                letter_contents = letter.read()
                personalized_letter = letter_contents.replace(PLACEHOLDER, name)
            recipient_email = record["email"]
            with mail.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=pw)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=recipient_email,
                    msg=f"Subject: Happy Birthday {name}!\n\n"
                        f"{personalized_letter}"
                )
            print(f"{letter} was personalized and sent to {name} at {recipient_email} from {my_email}.")


birthday_wish()
