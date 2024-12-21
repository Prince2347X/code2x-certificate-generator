import csv
import smtplib
from utils import generate_certificate
from utils.mail import send_certificate_email

output_dir = "certificates"

if __name__ == "__main__":
    from_email = ""
    from_password = ""

    # Connect to the SMTP server once
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, from_password)

    with open("participants.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            name, email = row
            output_filename = f"{output_dir}/{name} Code2X certificate.pdf"
            certificate_path = generate_certificate(name, output_filename)
            send_certificate_email(server, from_email, name, email, certificate_path)

    # Quit the server after sending all emails
    server.quit()

print("Certificates generated and emails sent successfully!")
