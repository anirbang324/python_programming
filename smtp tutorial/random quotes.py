import smtplib
import datetime as dt
import random

SENDER = "anirbantest72@gmail.com"
PASSWORD = "44123987"
#RECEIVER = "anirbang324@gmail.com"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 6:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    print(quote)

connection = smtplib.SMTP("smtp.gmail.com")
#connection = smtplib.SMTP("smtp.mail.yahoo.com")
connection.starttls()
connection.login(user=SENDER,password=PASSWORD)
connection.sendmail(from_addr=SENDER,
                    to_addrs="anirbang324@gmail.com",
                    msg=f"Subject:Monday Motivation\n\n{quote}"
                )
connection.close()