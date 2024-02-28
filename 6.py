# 6)Write a Python program that reads email details (sender, recipient, subject, and body) from user input and sends the email using Mailtrap as the SMTP server.


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, recipient_email, subject, body):
    smtp_server = "smtp.mailtrap.io"
    smtp_port = 587
    smtp_username = "your_username"
    smtp_password = "your_password"

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = subject

    message.attach(MIMEText(body, "plain"))

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.login(smtp_username, smtp_password)

        server.sendmail(sender_email, recipient_email, message.as_string())

sender_email = input("Enter your email address: ")
recipient_email = input("Enter the recipient's email address: ")
subject = input("Enter the email subject: ")
body = input("Enter the email body: ")

try:
    send_email(sender_email, recipient_email, subject, body)
    print("Email sent successfully!")
except Exception as e:
    print(f"An error occurred: {e}")
