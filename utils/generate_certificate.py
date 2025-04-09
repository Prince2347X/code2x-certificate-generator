from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import stringWidth

from utils.calculate_font_size import calculate_font_size

template_pdf = "code2x_template.pdf"
csv_file = "names.csv"

# Register the custom font
custom_font_path = "font/Virtual-Regular.ttf"
custom_font_name = "Virtual"
pdfmetrics.registerFont(TTFont(custom_font_name, custom_font_path))

# Change the font to the custom font
cursive_font = custom_font_name


# Generate individual PDFs
def generate_certificate(name, output_filename):
    # Step 1: Create a canvas overlay with the name in cursive font
    overlay_pdf = "overlay.pdf"
    c = canvas.Canvas(overlay_pdf, pagesize=letter)

    # Calculate dynamic font size
    dynamic_font_size = calculate_font_size(name)
    c.setFont(cursive_font, dynamic_font_size)

    # Set text color to white
    c.setFillColorRGB(1, 1, 1)

    # Calculate the width of the name and adjust the x-coordinate to center it
    name_width = stringWidth(name, cursive_font, dynamic_font_size)
    page_width = letter[0]
    x = (page_width + 350 - name_width) / 2
    y = 320

    c.drawString(x, y, name)
    c.save()

    # Step 2: Merge the overlay with the template
    template_reader = PdfReader(template_pdf)
    overlay_reader = PdfReader(overlay_pdf)
    writer = PdfWriter()

    for page in template_reader.pages:
        overlay_page = overlay_reader.pages[0]
        page.merge_page(overlay_page)
        writer.add_page(page)

    # Step 3: Write the output PDF
    with open(output_filename, "wb") as output_file:
        writer.write(output_file)
    print(f"Generated certificate for {name} at {output_filename}")
    return output_filename
