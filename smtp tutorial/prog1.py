import smtplib
my_email = "goswamianirban143@yahoo.com"
password = "ardo vjwi wzls yguk"
#we have to create app password for yahoo
#connection = smtplib.SMTP("smtp.gmail.com")
connection = smtplib.SMTP("smtp.mail.yahoo.com")
connection.starttls() #to establish a secure connection
connection.login(user=my_email,password=password)
connection.sendmail(from_addr=my_email,
                    to_addrs="anirbang324@gmail.com",
                    msg="This email is send using python."
                )
connection.close()