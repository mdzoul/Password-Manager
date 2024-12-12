from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ------------------------------ PASSWORD GENERATOR ------------------------------- #
def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.choices(letters, k=random.randint(8, 10))
    nr_symbols = random.choices(symbols, k=random.randint(2, 4))
    nr_numbers = random.choices(numbers, k=random.randint(2, 4))

    combine_letnumsym = nr_letters + nr_symbols + nr_numbers
    randomized_letnumsym = random.sample(combine_letnumsym, len(combine_letnumsym))

    new_password = "".join(randomized_letnumsym)
    pyperclip.copy(new_password)

    password_input.delete(0, END)
    password_input.insert(END, new_password)


# ------------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = site_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website.lower(): {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="Error: Empty fields", message="Do not leave any fields empty.")
    else:
        try:
            with open("password_manager.json", "r") as passwords:
                # Reading old data
                data = json.load(passwords)
        except FileNotFoundError:
            with open("password_manager.json", "w") as passwords:
                # Saving new data
                json.dump(new_data, passwords, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("password_manager.json", "w") as passwords:
                # Saving updated data
                json.dump(data, passwords, indent=4)
        finally:
            site_input.delete(0, END)
            password_input.delete(0, END)
            site_input.focus()


# ------------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    search_site = site_input.get()

    try:
        with open("password_manager.json", "r") as passwords:
            data = json.load(passwords)
            data_dict = data[search_site.lower()]
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found.")
    except KeyError:
        messagebox.showerror(title="Error", message=f"No details for {search_site.title()} exists.")
    else:
        messagebox.showinfo(title=f"{search_site}",
                            message=f"Email: {data_dict.get('email')} \nPassword: {data_dict.get('password')}")


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
site_input = Entry(width=22)
site_input.grid(row=2, column=2)
site_input.focus()
site_input.bind("<Return>", lambda funct1: email_input.focus())

email_input = Entry(width=39)
email_input.grid(row=3, column=2, columnspan=2)
email_input.insert(END, "user@email.com")
email_input.bind("<Return>", lambda funct1: password_input.focus())

password_input = Entry(width=22)
password_input.grid(row=4, column=2)

# Buttons
search_btn = Button(text="Search", width=13, command=find_password)
search_btn.grid(row=2, column=3)

password_btn = Button(text="Generate Password", command=gen_password)
password_btn.grid(row=4, column=3)

add_btn = Button(text="Add", width=36, command=save)
add_btn.grid(row=5, column=2, columnspan=2)

window.mainloop()
