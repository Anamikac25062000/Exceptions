# 8)write a python program to handle exceptions when sending emails using Python's smtplib library.


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, recipient_emails, subject, body):
    try:
        smtp_server = "smtp.mailtrap.io"
        smtp_port = 587
        smtp_username = "your_username"
        smtp_password = "your_password"

        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = ", ".join(recipient_emails)
        message["Subject"] = subject

        message.attach(MIMEText(body, "plain"))

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.login(smtp_username, smtp_password)

            server.sendmail(sender_email, recipient_emails, message.as_string())

        print("Email sent successfully!")

    except smtplib.SMTPException as smtp_exception:
        print(f"SMTP Exception: {smtp_exception}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

sender_email = input("Enter your email address: ")
recipient_emails = input("Enter the recipient email addresses separated by commas: ").split(',')
subject = input("Enter the email subject: ")
body = input("Enter the email body: ")

send_email(sender_email, recipient_emails, subject, body)
