import tkinter as tk
from tkinter import messagebox, ttk
import random

cvv_codes = [
    "123", "456", "789", "234", "987", "654", "321", "876", "543", "210",
    "111", "222", "333", "444", "555", "666", "777", "888", "999", "000"
]

credit_cards = [
    "3456 7890 1234 5678",  
    "4567 8901 2345 6789",
    "9876 5432 8765 4321",
    "1234 5678 8738 4321",
    "2345 6789 3456 7890",
    "8765 4321 2345 6789",
    "5678 9012 3456 7890",
    "6789 0123 1234 5678",
    "3456 7812 8765 4321",
    "7890 1234 5678 9012"
]

expiration_1 = [
    "01/26", "05/27", "12/29", "08/23", "11/24", "02/25", "07/30", "03/28",
    "09/22", "06/31", "10/25", "04/26", "03/29", "12/31", "01/24",
    "06/27", "07/25", "11/28", "10/23", "02/26", "09/30"
]

bank12 = [
    "Chase Bank", "Bank of America", "Citibank", "Wells Fargo", "HSBC",
    "PNC Bank", "Capital One", "American Express Bank", "U.S. Bank",
    "Barclays", "TD Bank", "Santander Bank"
]

def generate_card():
    try:
        age = int(age_entry.get())
        if age < 18:
            messagebox.showwarning("Underage", "UNDERAGE: CANNOT SIGN UP FOR CREDIT CARD")
            return
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid age.")
        return

    first_name = first_name_entry.get().strip().capitalize()
    last_name = last_name_entry.get().strip().capitalize()

    if not first_name or not last_name:
        messagebox.showerror("Missing Info", "Please fill in both first and last names.")
        return

    progress_bar.grid(row=6, column=0, columnspan=2, pady=10)
    progress_bar.start(10)
    root.after(1500, lambda: finish_card_generation(first_name, last_name))

def finish_card_generation(first_name, last_name):
    progress_bar.stop()
    progress_bar.grid_remove()

    card_number = random.choice(credit_cards)
    expiration = random.choice(expiration_1)
    cvv = random.choice(cvv_codes)
    bank = random.choice(bank12)

    result = (
        f"Card Number: {card_number}\n"
        f"Full Name: Mr. {last_name} {first_name}\n"
        f"Expiration Date: {expiration}\n"
        f"CVV: {cvv}\n"
        f"Issuer: {bank}"
    )
    result_label.config(text=result)

root = tk.Tk()
root.title("Credit Card Sign-Up")
root.geometry("420x420")

tk.Label(root, text="Enter your age:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
age_entry = tk.Entry(root)
age_entry.grid(row=0, column=1, padx=10)

tk.Label(root, text="First Name:").grid(row=1, column=0, sticky="w", padx=10, pady=5)
first_name_entry = tk.Entry(root)
first_name_entry.grid(row=1, column=1, padx=10)

tk.Label(root, text="Last Name:").grid(row=2, column=0, sticky="w", padx=10, pady=5)
last_name_entry = tk.Entry(root)
last_name_entry.grid(row=2, column=1, padx=10)

tk.Button(root, text="Generate Card", command=generate_card).grid(row=3, column=0, columnspan=2, pady=20)

style = ttk.Style()
style.configure("green.Horizontal.TProgressbar", troughcolor='white', background='limegreen')
progress_bar = ttk.Progressbar(root, style="green.Horizontal.TProgressbar", mode='indeterminate', length=300)

result_label = tk.Label(root, text="", justify="left", font=("Courier", 10))
result_label.grid(row=7, column=0, columnspan=2, pady=10, padx=10)

root.mainloop()
