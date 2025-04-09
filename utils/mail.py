from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os


def send_certificate_email(server, from_email, name, email, certificate_path):
    subject = "Certification of Participation - Code2X"
    body = f"Dear {name},\nThank you for participating in our coding competition - Code2X. It was a pleasure to witness your enthusiasm and problem solving skills.\n\nAs a token of appreciation, please find the attached Certificate of Participation. We look forward to your contribution in future events.\n\n\nBest regards,\nCode2X Team\nStudent Activity Centre"

    # Create the email
    msg = MIMEMultipart()
    msg["From"] = from_email
    msg["To"] = email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    # Attach the certificate
    attachment = open(certificate_path, "rb")
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {os.path.basename(certificate_path)}",
    )
    msg.attach(part)

    # Send the email
    print(f"Sending mail to {name} - {email}")
    text = msg.as_string()
    server.sendmail(from_email, email, text)
    print(f"Sent mail to {email} ✅")
