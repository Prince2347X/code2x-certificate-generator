# import csv
from utils import generate_certificate

output_dir = "certificates"

if __name__ == "__main__":
    # with open("names.csv", "r") as file:
    #     reader = csv.reader(file)
    #     next(reader)

    #     for row in reader:
    #         name = row[0]
    #         output_filename = f"{output_dir}/{name} Code2X certificate.pdf"
    #         generate_certificate(name, output_filename)
    name = "John Doe"
    output_filename = f"{output_dir}/{name} Code2X certificate.pdf"
    generate_certificate(name, output_filename)

print("Certificates generated successfully!")
