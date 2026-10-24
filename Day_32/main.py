##################### Extra Hard Starting Project ######################
import smtplib
import random
import pandas
import datetime as dt

my_email = "umathileepan@gmail.com"
password = "arvi kchf vryk qyxj"

birthday_details = pandas.read_csv("birthdays.csv")
birthday_data = birthday_details.to_dict()
now = dt.datetime.now()
current_day = now.day
current_month = now.month
birthday_day = birthday_data["day"]
birthday_month = birthday_data["month"]

letter_files = ["letter_1.txt","letter_2.txt","letter_2.txt"]
selected_letter = random.choice(letter_files)

for index, row in birthday_details.iterrows():
    if row["month"] == current_month and row["day"] == current_day:
        #print(f"Today is {row['name']}'s birthday!")
        names = row['name']
        with open(f"./letter_templates/{selected_letter}", mode="r") as name_letter:
            # Replace the [name] placeholder with the actual name.
            search_text = "[NAME]"
            file = name_letter.read()
            clean_name = names.strip()
            content = file.replace(search_text, clean_name)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()   #Transport Layer Security secure the connection
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,to_addrs="thileepan_uma@yahoo.co.uk",msg=f"Subject: Birthday Wishes\n\n {content}")












#

# 4. Send the letter generated in step 3 to that person's email address.




