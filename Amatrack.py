import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
load_dotenv()

#  -- IMPORTANT --
#  The program will not work unless you go to .env and put in your own sender email
#  and app password.



TRACKED_ITEM = "https://www.amazon.com/Instant-Pot-Plus-60-Programmable/dp/B01NBKTPTS/ref=sr_1_3?crid=1KRFYZJ3Y3KRG&dib=eyJ2IjoiMSJ9.g1Lrz7oNcd8sVDvjEfcK4woQFm3qlOqvoway1SDbaoULS1Nwqmv6TMdtirBwQUf2JFrBp7XWTIuZ6_QzrfE9miLxMz-6MaNzCb2ANcD5ruJUuDjWf0wNw9SM2GB9n4OyJCOdsPYi3hfB5kQaBFubFeniSJYoLFzAwVEgV285wfsT444yMlTl_ZOFZt4ooeBIdnrI8KAKteARjS8NWpz1MA_aO2wjUdi9_ZNAklL48Uc.jAub4krK-kXCkabZxn0DahRnl-3V3DCQat6dr7zoz0I&dib_tag=se&keywords=instant%2Bpot&qid=1753585176&sprefix=instant%2Bpot%2Caps%2C557&sr=8-3&th=1"
TARGET_PRICE = 500.00
EMAIL = "burakacarburakacar@gmail.com"



#Make a function to send an email
def sendemail(smtpaddress, youremail, yourAPPpassword, recipientemail, subject, contents):
    import smtplib
    myemail = youremail
    password= yourAPPpassword

    with smtplib.SMTP(smtpaddress) as connection:
        connection.starttls()
        connection.login(user=myemail, password=password)
        connection.sendmail(from_addr=youremail, to_addrs=recipientemail, msg=f"Subject:{subject} \n\n {contents}")


request = requests.get(TRACKED_ITEM, headers={"Accept-Language":"en-US"})
websiteo = request.text
print(websiteo)
website = BeautifulSoup(websiteo, "html.parser")

price = float(website.find("span", class_="aok-offscreen").get_text(strip=True).split("$")[1])

if price < TARGET_PRICE:
    sendemail(
        smtpaddress="smtp.gmail.com",
        youremail=os.getenv("senderEmail"),
        yourAPPpassword=os.getenv("appPasswordGoogle"),
        recipientemail=EMAIL,
        subject="LOW PRICE ALERT!",
        contents=f"The price of your tracked item has dropped to ${price}. Check it out at {TRACKED_ITEM}",
    )
