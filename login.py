from customtkinter import *
from PIL import Image
import sqlite3

# Initialize main window
main = CTk()
main.title("Login Page")
main.config(bg="white")
main.resizable(False, False)

# Load background image
bg_img = CTkImage(dark_image=Image.open("images/bg1.jpg"), size=(500, 500))

# Create background label
bg_lab = CTkLabel(main, image=bg_img, text="")
bg_lab.grid(row=0, column=0)

# Create frame for login form
frame1 = CTkFrame(main, fg_color="#D9D9D9", bg_color="white", height=350, width=300, corner_radius=20)
frame1.grid(row=0, column=1, padx=40)

# Add title to login frame
title = CTkLabel(frame1, text="Welcome Back! \nLogin to Account", text_color="black", font=("", 35, "bold"))
title.grid(row=0, column=0, sticky="nw", pady=30, padx=10)

# Create username entry
usrname_entry = CTkEntry(frame1, text_color="white", placeholder_text="Username", fg_color="black", placeholder_text_color="white",
                         font=("", 16, "bold"), width=200, corner_radius=15, height=45)
usrname_entry.grid(row=1, column=0, sticky="nwe", padx=30)

# Create password entry
passwd_entry = CTkEntry(frame1, text_color="white", placeholder_text="Password", fg_color="black", placeholder_text_color="white",
                         font=("", 16, "bold"), width=200, corner_radius=15, height=45, show="*")
passwd_entry.grid(row=2, column=0, sticky="nwe", padx=30, pady=20)

# Function to open the create account window
def open_create_account_window():
    create_account_window = CTkToplevel(main)
    create_account_window.title("Create Account")
    create_account_window.geometry("400x300")
    create_account_window.config(bg="white")

    # Add form elements for creating account
    title = CTkLabel(create_account_window, text="Create Account", text_color="black", font=("", 25, "bold"))
    title.pack(pady=20)

    new_usrname_entry = CTkEntry(create_account_window, text_color="white", placeholder_text="New Username", fg_color="black", placeholder_text_color="white",
                         font=("", 16, "bold"), width=200, corner_radius=15, height=45)
    new_usrname_entry.pack(pady=10)

    new_passwd_entry = CTkEntry(create_account_window, text_color="white", placeholder_text="New Password", fg_color="black", placeholder_text_color="white",
                         font=("", 16, "bold"), width=200, corner_radius=15, height=45, show="*")
    new_passwd_entry.pack(pady=10)

    def create_account():
        username = new_usrname_entry.get()
        password = new_passwd_entry.get()
        # Add your database logic here to create a new account
        with sqlite3.connect('users.db') as conn:
            cursor = conn.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
        create_account_window.destroy()

    create_acc_btn = CTkButton(create_account_window, text="Create Account", font=("", 15, "bold"), height=40, width=200, fg_color="#0085FF",
                               cursor="hand2", corner_radius=15, command=create_account)
    create_acc_btn.pack(pady=20)

# Create account label and bind click event
cr_acc = CTkLabel(frame1, text="Create Account!", text_color="black", cursor="hand2", font=("", 15))
cr_acc.grid(row=3, column=0, sticky="w", pady=20, padx=40)
cr_acc.bind("<Button-1>", lambda e: open_create_account_window())

# Login button (add functionality as needed)
l_btn = CTkButton(frame1, text="Login", font=("", 15, "bold"), height=40, width=60, fg_color="#0085FF", cursor="hand2",
                  corner_radius=15)
l_btn.grid(row=3, column=0, sticky="ne", pady=20, padx=35)

# Main loop
main.mainloop()
