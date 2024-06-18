import os
import csv
# import hashlib
import tkinter as tk
from tkinter import filedialog
import pandas as pd

def generate_email(first_name, last_name, year):
    email = f"{first_name.replace(' ', '.')}.{last_name.replace(' ', '.')}.{year}@calvino.edu.it"
    return email

def generate_password():
    return "Calvino2025!"

# def generate_password_hash(password):
#     return hashlib.sha256(password.encode()).hexdigest()

def process_file():
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xls;*.xlsx")])
    if file_path:
        df = pd.read_excel(file_path)
        data = []
        for _, row in df.iterrows():
            first_name = row["NOME"]
            last_name = row["COGNOME"]
            year = str(row["AN"])
            email = generate_email(first_name, last_name, year)
            password = generate_password()
            # password_hash = generate_password_hash(password)
            data.append({
                "First Name [Required]": first_name,
                "Last Name [Required]": last_name,
                "Email Address [Required]": email,
                "Password [Required]": password,
                # "Password Hash Function [UPLOAD ONLY]": password_hash,
                "Org Unit Path [Required]": "/Studenti",
                # "New Primary Email [UPLOAD ONLY]": email,
                "Change Password at Next Sign-In": "TRUE"
            })

        output_file = os.path.splitext(os.path.basename(file_path))[0] + ".csv"
        with open(output_file, "w", newline="") as csvfile:
            fieldnames = list(data[0].keys())
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        print(f"CSV file saved: {output_file}")

root = tk.Tk()
root.title("XLS to CSV Converter")

open_button = tk.Button(root, text="Open XLS File", command=process_file)
open_button.pack(pady=20)

root.mainloop()