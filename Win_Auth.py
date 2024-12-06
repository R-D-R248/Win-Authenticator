#importing all necessary libraries
import tkinter as tk
from tkinter import messagebox
import os

#Obtaining Username
username = os.getlogin()

# Path for the password file
path_pass = f"C:\\Users\\{username}\\Desktop\\password_auth.txt"

# Ensure the directory exists
directory = os.path.dirname(path_pass)
if not os.path.exists(directory):
    os.makedirs(directory)

# Validate if the user has an account
if os.path.exists(path_pass):
    try:
        with open(path_pass) as f:
            acc = 1
    except FileNotFoundError:
        acc = 0
else:
    acc = 0

#if user has an account
if acc == 1:
    # Set screen
    screen = tk.Tk()
    screen.attributes("-fullscreen", True)
    with open(path_pass, 'r') as file:
        pas = file.read().strip()

    # Label
    label = tk.Label(screen, text=f"Welcome {username}!", font=("Arial", 16))
    label2 = tk.Label(screen, text="Please Enter your password", font=("Arial", 12))

    # Password entry
    password_label = tk.Label(screen, text="Password:", font=("Arial", 14))
    password_label.pack(pady=5)
    password_entry = tk.Entry(screen, show="•", font=("Arial", 14))
    password_entry.pack(pady=10)
    label.pack()
    label2.pack()

    # Password check function
    def login():
        entered_password = password_entry.get()
        if entered_password == pas:
            messagebox.showinfo("Login Successful", f"Welcome, {username}!")
            screen.destroy()
        else:
            messagebox.showerror("Login Failed", "Invalid Password. Please try again.")

    # Login Button
    login_button = tk.Button(screen, text="Login", command=login, font=("Arial", 14), bg="lightblue", width=10)
    login_button.pack(pady=20)
    screen.mainloop()

else:
    print("Welcome to Win Authenticator! Please Choose a Password")
    while True:
        password = input("Password: ")
        if password == "":
            print("Password is Empty!\n")
        elif not any(char.isdigit() for char in password):
            print("Password must contain at least one Number.\n")
        elif not any(char.isalpha() for char in password):
            print("Password must contain at least one Letter.\n")
        elif not any(char.isupper() for char in password):
            print("Password must contain at least one Uppercase Letter.")
        elif not any(char in "!@#$%^&*(){}[]<>?/:;" for char in password):
            print("Password must contain at least one Special Character.\n")
        elif any(char.isspace() for char in password):
            print("Password shouldn't contain spaces.\n")
        elif len(password) <= 5:
            print("Password must contain at least five characters.\n")
        else:
            break
    # Create the password file
    with open(path_pass, "w") as file:
        file.write(password)
    print(input("\nClick Enter to Exit"))
quit
