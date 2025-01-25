import os
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv()#Load the environment variables

def check_website(url):
    try:
        response = requests.get(url, timeout=5)  # Added timeout to prevent hanging
        print(response)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False

def send_email(sender_email, receiver_email, password, subject, body):
    message = MIMEMultipart()  # Fixed incorrect initialization
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    message.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send the email: {e}")

url = "https://fakestoreapi.org"
if not check_website(url):
    sender_email = "e3678448@gmail.com"
    receiver_email = "fdhk895@gmail.com"
    password =  os.getenv("APP_PASSWORD")
    subject = "Website is not working"
    body = "The application is in a terminated state"

    send_email(sender_email, receiver_email, password, subject, body)
else:
    print("The website is up")
