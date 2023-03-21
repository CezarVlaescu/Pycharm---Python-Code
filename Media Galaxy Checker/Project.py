from lxml import html
import requests
from time import sleep
import time
import schedule
import smtplib

# Email id for who want to check availability

receiver_email_id = "vlaescucezar@yahoo.com"

def check(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                             '(KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
    page = requests.get(url, headers=headers)
    for i in range(20):
        sleep(3)
        doc = html.fromstring(page.content)

        # Check availability

        XPATH_AVAILABILITY = '//div[@id="_next"]//text()'
        Raw_Availability = doc.xpath(XPATH_AVAILABILITY)
        Availability = ''.join(Raw_Availability).strip() if Raw_Availability else None
        return Availability

def sendmail(ans, product):
    Email_username = "vlaescucezar@yahoo.com"
    Email_password = "********"

    recipient = receiver_email_id
    email_body = ans
    email_subject = product + 'product availability'

    # Create a SMTP session

    s = smtplib.SMTP('smtp@yahoo.com', 587)

    # Starting TLS for security

    s.starttls()

    # Authentication

    s.login(Email_username, Email_password)

    # Sending message

    headers = "\r\n".join(["from: " + Email_username,
                          "subject: " + email_subject,
                          "to: " + recipient,
                          "mime-version: 1.0",
                          "content-type: text/html"])

    content = headers + "\r\n\r\n" + email_body
    s.sendmail(Email_username, recipient, content)
    s.quit()

def ReadAsin():
    Asin = 'CASRPT01BK' # Product ID from site
    url = "https://mediagalaxy.ro/casti-adidas-rpt-01-bluetooth-on-ear-microfon-night-grey/cpd/" + Asin
    print("Processing: " + url)
    ans = check(url)
    arr = ["Only 1 left in stock.",
           "Only 2 left in stock.",
           "In stock."]
    print(ans)
    if ans in arr:
        # Send the email to user if the product is available
        sendmail(ans, Asin)

def job():
    print("Tracking....")
    ReadAsin()
schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)









