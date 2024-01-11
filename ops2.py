import smtplib
from email.mime.text import MIMEText

def send_notification(host, status):
    message = MIMEText(f"Host {host} is now {status}.")
    message['Subject'] = f"Host Update: {host}"
    message['From'] = "your_email@example.com"
    message['To'] = "admin@example.com"

    with smtplib.SMTP("smtp.example.com", 587) as server:
        server.starttls()
        server.login("your_email", "your_password")
        server.send_message(message)

# Replace with your host and initial status
host = "example.com"
status = "up"

while True:
    # Update status with your actual checks
    new_status = check_host_status(host)
    if new_status != status:
        send_notification(host, new_status)
        status = new_status
    time.sleep(60)


Atrributions
https://bard.google.com/
https://bard.google.com/
https://stackoverflow.com/questions/16405874/automate-smtp-using-python
