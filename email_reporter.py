import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_commit_email(subject: str, body: str):
    sender = os.getenv("EMAIL_HOST_USER")
    receiver = os.getenv("EMAIL_RECEIVER")
    port = os.getenv("EMAIL_PORT")

    print(f"📬 Email config — Host: {os.getenv('EMAIL_HOST')}, Port: {port}, Sender: {sender}, Receiver: {receiver}")

    if port is None:
        raise ValueError("EMAIL_PORT environment variable is not set")

    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP(os.getenv("EMAIL_HOST"), int(port)) as server:
            server.starttls()
            server.login(sender, os.getenv("EMAIL_HOST_PASSWORD"))
            server.send_message(msg)
        print("📧 Email sent successfully.")
    except Exception as e:
        print("❌ Email failed:", e)
