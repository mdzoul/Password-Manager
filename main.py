from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ------------------------------ PASSWORD GENERATOR ------------------------------- #
def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.choices(letters, k=random.randint(8, 10))
    nr_symbols = random.choices(symbols, k=random.randint(2, 4))
    nr_numbers = random.choices(numbers, k=random.randint(2, 14))

    combine_letnumsym = nr_letters + nr_symbols + nr_numbers
    randomized_letnumsym = random.sample(combine_letnumsym, len(combine_letnumsym))

    new_password = "".join(randomized_letnumsym)
    pyperclip.copy(new_password)
    messagebox.showinfo(title="Password saved", message="Password saved to clipboard")

    password_input.delete(0, END)
    password_input.insert(END, new_password)


# ------------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = site_input.get()
    email = email_input.get()
    password = password_input.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Error: Empty fields", message="Do not leave any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title="Save details?",
                                       message=f"Website: {website} \nEmail: {email} \nPassword: {password} "
                                               f"\nOK to save?")
        if is_ok:
            with open("password_manager.txt", "a") as passwords:
                passwords.write(f"{website} | {email} | {password}\n")
                site_input.delete(0, END)
                password_input.delete(0, END)
                site_input.focus()


# ------------------------------ UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# MyPass image
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=1, column=1, columnspan=3)

# Labels
site_label = Label(text="Website:")
site_label.grid(row=2, column=1)

email_label = Label(text="Email/Username:")
email_label.grid(row=3, column=1)

password_label = Label(text="Password:")
password_label.grid(row=4, column=1)

# Entries
site_input = Entry(width=39)
site_input.grid(row=2, column=2, columnspan=2)
site_input.focus()
site_input.bind("<Return>", lambda funct1: email_input.focus())

email_input = Entry(width=39)
email_input.grid(row=3, column=2, columnspan=2)
email_input.insert(END, "user@email.com")
email_input.bind("<Return>", lambda funct1: password_input.focus())

password_input = Entry(width=22)
password_input.grid(row=4, column=2)

# Buttons
password_btn = Button(text="Generate Password", command=gen_password)
password_btn.grid(row=4, column=3)

add_btn = Button(text="Add", width=36, command=save)
add_btn.grid(row=5, column=2, columnspan=2)

window.mainloop()
