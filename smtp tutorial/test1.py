import smtplib

email = "flashofearth23@gmail.com"
pwd = "osoB2Dummy"
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(email,pwd)
connection.sendmail(from_addr= email,to_addrs="anirbang324@gmail.com",msg="Subject:Hi there/n Hello from Aryan!")
connection.close()