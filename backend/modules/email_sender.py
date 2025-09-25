import os
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

# You need to fill in your email details here.
# For Gmail, you must use an "App Password" for security, NOT your regular password.
SENDER_EMAIL = "srujanag521@gmail.com"  # <--- Your Gmail address
SENDER_PASSWORD = "wunlmpnkpvqhlvou"  # <--- Your Gmail App Password
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

def send_email_with_attachment(recipient_email, report_name, attachment_path):
    """
    Connects to the SMTP server and sends the email with the attached report.
    """
    try:
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = recipient_email
        msg['Subject'] = f"Financial Report: {report_name}"

        body = f"Hello,\n\nPlease find the requested financial report attached.\n\nReport Name: {report_name}\n\nBest regards,\nYour Reporting App"
        msg.attach(MIMEText(body, 'plain'))

        with open(attachment_path, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        encoders.encode_base64(part)
        part.add_header("Content-Disposition", f"attachment; filename= {os.path.basename(attachment_path)}")
        msg.attach(part)

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        text = msg.as_string()
        server.sendmail(SENDER_EMAIL, recipient_email, text)
        server.quit()
        print(f"Email sent successfully to {recipient_email}")
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False


