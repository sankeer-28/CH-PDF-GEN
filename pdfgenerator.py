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
    answers = []
    for p in range(5):
        pdf.add_page()
        if p == 0:
            pdf.set_font("Arial", style='B', size=16)
            pdf.cell(200, 10, txt="Random Math Problems", ln=1, align='C')
            pdf.set_font("Arial", size=12)
        else:
            pdf.set_font("Arial", size=12)
        for j in range(34):
            num_operands = random.randint(2, 5)
            equation1 = f"{random.randint(0, 10**(random.randint(1, 3))-1)}"
            equation2 = f"{random.randint(0, 10**(random.randint(1, 3))-1)}"
            equation3 = f"{random.randint(0, 10**(random.randint(1, 3))-1)}"
            for k in range(num_operands-1):
                equation1 += f" {random.choice(operators)} {random.randint(0, 10**(random.randint(1, 3))-1)}"
                equation2 += f" {random.choice(operators)} {random.randint(0, 10**(random.randint(1, 3))-1)}"
                equation3 += f" {random.choice(operators)} {random.randint(0, 10**(random.randint(1, 3))-1)}"
            try:
                answer1 = round(eval(equation1), 2)
                answer2 = round(eval(equation2), 2)
                answer3 = round(eval(equation3), 2)
            except ZeroDivisionError:
                j -= 1
                continue
            answers.extend([answer1, answer2, answer3])
            equation_number = p*102 + j*3 + 1
            equation1 = f"{equation_number}) {equation1} ="
            equation2 = f"{equation_number+1}) {equation2} ="
            equation3 = f"{equation_number+2}) {equation3} ="
            pdf.cell(63, 10, txt=equation1, ln=0, align='L')
            pdf.cell(63, 10, txt=equation2, ln=0, align='C')
            pdf.cell(63, 10, txt=equation3, ln=1, align='R')
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Answer Key", ln=1, align='C')
    for idx in range(len(answers)):
        pdf.cell(63.33 if idx % 3 == 0 else (63.33 if idx % 3 == 2 else 0), 10,
                 txt=f"{idx+1}. {answers[idx]}", ln=idx % 3 == 2 or idx == len(answers)-1,
                 align='L' if idx % 3 == 0 else ('C' if idx % 3 == 1 else 'R'))
    filename = os.path.join(folder_path, f"{generate_random_filename()}.pdf")
    pdf.output(filename)
