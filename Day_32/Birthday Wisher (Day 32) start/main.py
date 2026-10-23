import smtplib

my_email = "umathileepan@gmail.com"
password = "arvi kchf vryk qyxj"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()   #Transport Layer Security secure the connection
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,to_addrs="thileepan_uma@yahoo.co.uk",msg="Subject: Hello\n\n This is a test message.")

