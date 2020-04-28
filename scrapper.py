import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = input("Please enter the URL for comparison: ")

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.123 Safari/537.36'}


def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    # title = soup.find(id="-fs20 -pts -pbxs").get_text()
    title1 = soup.find('div', attrs={"class": "-fs0 -pls -prl"}).get_text()
    price1 = soup.find('span', attrs={"class": "-b -ltr -tal -fs24"}).get_text()
    # convertedprice = price1.replace("KSh,", "")
    convertedprice = price1.translate({ord(i): None for i in 'KSh,'})
    removespaces = convertedprice.translate({ord(i): None for i in ' '})
    # s.translate({ord(i): None for i in 'abc'})
    changetofloat = float(removespaces)

    if changetofloat > 500:
        # send_mail()
        print(title1)
        print(changetofloat)
    else:
        print("The product " + title1 + " Is worth " + str(changetofloat) + " which is less than the 500 threshold")


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('kevinblac1@gmail.com', 'bmqwesssuhixcgmx')

    subject = "price is still upwards"
    body = "Check the link on jumia: " + URL

    msg = f"subject:{subject}\n\n{body}"

    server.sendmail(
        'kevinblac1@gmail.com',
        'couch@vivaldi.net',
        msg
    )

    print("Hey Email has been Sent")

    server.quit()

#while True:
check_price()
    #time.sleep(60*60)

