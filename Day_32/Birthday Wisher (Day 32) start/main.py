import smtplib
import datetime as dt
import random

now = dt.datetime.now()
#year = now.year
#print(year)
#birth_day = dt.datetime(year=1995,month=9,day=9)
#print(birth_day)
day_of_week = now.weekday()

with open("quotes.txt","r") as quotes:
    quotes_list = quotes.readlines()
    my_greeting = random.choice(quotes_list)
    if day_of_week == 0:
        my_greeting_day = "Monday Motivation"
    elif day_of_week == 1:
        my_greeting_day = "Tuesday Motivation"
    elif day_of_week == 2:
        my_greeting_day = "Wednesday Motivation"
    elif day_of_week == 3:
        my_greeting_day = "Thursday Motivation"
    elif day_of_week == 4:
        my_greeting_day = "Friday Motivation"
#year = now.year
#print(year)
#birth_day = dt.datetime(year=1995,month=9,day=9)
#print(birth_day)
day_of_week = now.weekday()
print(day_of_week)

my_email = "umathileepan@gmail.com"
password = "arvi kchf vryk qyxj"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()   #Transport Layer Security secure the connection
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,to_addrs="thileepan_uma@yahoo.co.uk",msg=f"Subject: {my_greeting_day}\n\n {my_greeting}")



