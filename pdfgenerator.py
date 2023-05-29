import os
import random
import string
from fpdf import FPDF

# Function to generate a random filename
def generate_random_filename(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

# Create a new directory in the Downloads folder
downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
folder_path = os.path.join(downloads_path, "generated_pdfs")
os.makedirs(folder_path, exist_ok=True)

operators = ['+', '-', '*', '/']
for i in range(1, 21):
    pdf = FPDF()
    for p in range(5):
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        for j in range(100):
            equation = f"{random.randint(1, 100)} {random.choice(operators)} {random.randint(1, 100)}"
            pdf.cell(200, 10, txt=equation, ln=j+1, align='C')
    filename = os.path.join(folder_path, f"{generate_random_filename()}.pdf")
    pdf.output(filename)
    print(os.getcwd())