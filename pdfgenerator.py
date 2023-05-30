# https://github.com/sankeer-28
import tkinter as tk
from tkinter import messagebox, filedialog
import os
import random
import string
from fpdf import FPDF

def generate_random_filename(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def generate_pdf(num_pdfs=None):
    # Get the number of PDFs to generate from the Entry widget
    if not num_pdfs:
        try:
            num_pdfs = int(num_pdfs_entry.get())
        except ValueError:
            messagebox.showerror("Error‼️", "Please enter a valid number ‼️‼️‼️")
            return

    # Create a new directory in the specified folder
    folder_path = os.path.join(download_location_entry.get(), "generated_pdfs")
    os.makedirs(folder_path, exist_ok=True)

    operators = ['+', '-', '*', '/']
    for i in range(num_pdfs):
        pdf = FPDF()
        answers = []
        for p in range(5):
            pdf.add_page()
            if p == 0:
                pdf.set_font("Arial", style='B', size=16)
                pdf.cell(200, 10, txt="Random Math Problems", ln=1, align='C')
                pdf.ln(10)
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
                equation_number = (p*102 if p == 0 else p*102 - 3) + j*3 + 1

                pdf.set_font("Arial", style='B', size=12)
                question_number = f"{equation_number})"
                w = pdf.get_string_width(question_number) + 2
                pdf.cell(w, 10, txt=question_number, ln=0)
                pdf.set_font("Arial", size=12)
                pdf.cell(63 - w, 10, txt=f" {equation1} =", ln=0)

                pdf.set_font("Arial", style='B', size=12)
                question_number = f"{equation_number+1})"
                w = pdf.get_string_width(question_number) + 2
                pdf.cell(w, 10, txt=question_number, ln=0)
                pdf.set_font("Arial", size=12)
                pdf.cell(63 - w, 10, txt=f" {equation2} =", ln=0)

                pdf.set_font("Arial", style='B', size=12)
                question_number = f"{equation_number+2})"
                w = pdf.get_string_width(question_number) + 2
                pdf.cell(w, 10, txt=question_number, ln=0)
                pdf.set_font("Arial", size=12)
                pdf.cell(63 - w, 10, txt=f" {equation3} =", ln=1)

        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Answer Key", ln=1, align='C')
        for idx in range(len(answers)):
            pdf.set_font("Arial", style='B', size=12)
            question_number = f"{idx+1})"
            w = pdf.get_string_width(question_number) + 2
            pdf.cell(w, 10, txt=question_number, ln=0)
            pdf.set_font("Arial", size=12)
            if idx % 3 == 0:
                pdf.cell(63 - w, 10, txt=f" {answers[idx]}", ln=0)
            elif idx % 3 == 1:
                pdf.cell(63 - w, 10, txt=f" {answers[idx]}", ln=0)
            else:
                pdf.cell(5, 10, txt="", ln=0)
                pdf.cell(w, 10, txt=f"{answers[idx]}", ln=1)
        filename = os.path.join(folder_path, f"{generate_random_filename()}.pdf")
        pdf.output(filename)
    messagebox.showinfo("Great Success", "PDFs generated!")

def browse_folder():
    folder_selected = filedialog.askdirectory()
    download_location_entry.delete(0, tk.END)
    download_location_entry.insert(0, folder_selected)

def update_button_text(*args):
    try:
        num_pdfs = int(num_pdfs_entry.get())
        generate_button_text.set(f"Generate {num_pdfs} PDFs")
    except ValueError:
        generate_button_text.set("Generate PDF")

root = tk.Tk()
root.title("PDF Generator 📝")
root.geometry("450x400")
root.config(bg="gray37")

title_label = tk.Label(root, text="Random Math PDF Generator 🎲", font=("Helvetica", 20, 'bold'),  bg="gray37", fg="white")
title_label.pack(padx=10, pady=10)

num_pdfs_label = tk.Label(root, text="Number of PDFs to generate:", font=("Helvetica", 16), bg="gray27", fg="white")
num_pdfs_label.pack(padx=10, pady=10)

num_pdfs_entry_var = tk.StringVar()
num_pdfs_entry_var.trace("w", update_button_text)
num_pdfs_entry = tk.Entry(root, textvariable=num_pdfs_entry_var)
num_pdfs_entry.pack(padx=10, pady=10)

generate_button_text = tk.StringVar()
generate_button_text.set("Generate PDF")
generate_button = tk.Button(root, textvariable=generate_button_text, command=generate_pdf, bg="gray27", fg="white")
generate_button.pack(padx=10, pady=10)

generate_20_button = tk.Button(root, text="Auto Generate 20 PDFs", command=lambda: generate_pdf(20), bg="gray27", fg="white")
generate_20_button.pack(padx=10, pady=10)

download_location_label = tk.Label(root, text="Download Location:", font=("Helvetica", 16), bg="gray27", fg="white")
download_location_label.pack(padx=10, pady=10)

download_location_entry = tk.Entry(root, width=30)
download_location_entry.insert(0, os.path.join(os.path.expanduser("~"), "Downloads"))
download_location_entry.pack(padx=10, pady=10)

browse_button = tk.Button(root, text="Change Download Location", command=browse_folder, bg="gray27", fg="white")
browse_button.pack(padx=10, pady=10)

custom_text_label = tk.Label(root, text="https://github.com/sankeer-28", font=("Helvetica", 8), bg="gray0", fg="white")
custom_text_label.place(relx=1.0,rely=1.0,x=-5,y=-5,anchor='se')

root.mainloop()
