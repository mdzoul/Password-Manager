# CHANGELOG
# Original file backed up on 2024-12-09
# Changes in this version:
#   1. Listbox for Multisearch:
#       - Integrated a Listbox to display multiple matches below the main search bar.
#       - Simplified layout for better alignment and usability.
#   2. Fuzzy Search Implementation:
#       - Enhanced the search functionality to support fuzzy matching using regular expressions.
#       - Matches are dynamically displayed in the Listbox.
#   3. Improved User Interaction:
#       - Users can select an item from the Listbox using the Enter key.
#       - After selection, the details of the selected item are displayed, and the Listbox is cleared.
#   4. Add login authentication functionality
#       - Implement user login form and validation logic
#       - Integrate authentication backend to verify user credentials

import re
import tkinter
from tkinter import messagebox
import random
import pyperclip
import json

def authenticate():
    # ------------------------------ CENTER WINDOW ------------------------------- #
    def center_window(win):
        win.update_idletasks()  # Ensures geometry information is up-to-date
        width = win.winfo_width()
        height = win.winfo_height()
        screen_width = win.winfo_screenwidth()
        screen_height = win.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        win.geometry(f"{width}x{height}+{x}+{y}")
        win.focus_force()  # Ensures the window gains focus

        
    # ------------------------------ AUTHENTICATOR ------------------------------- #
    MASTER_PASSWORD = "admin1234"

    def validate_password():
        entered_password = password_entry.get()
        if entered_password == MASTER_PASSWORD:
            login_window.destroy()
            main_application()
        else:
            messagebox.showerror("Access Denied", "Invalid password")
            password_entry.delete(0, tkinter.END)

    login_window = tkinter.Tk()
    login_window.title("Login")
    login_window.geometry("300x150")
    center_window(login_window)  # Center the authenticator window

    tkinter.Label(login_window, text="Enter Password:").pack(pady=10)

    password_entry = tkinter.Entry(login_window, show="*")
    password_entry.pack(pady=5)
    password_entry.focus_set()  # Automatically focus on the password entry field
    password_entry.bind("<Return>", lambda funct1: login_button.invoke())

    login_button = tkinter.Button(login_window, text="Login", command=validate_password)
    login_button.pack(pady=20)

    login_window.mainloop()


def main_application() -> None:
    # ------------------------------- CENTER WINDOW ------------------------------- #
    def center_window(win):
        win.update_idletasks()  # Ensures geometry information is up-to-date
        width = win.winfo_width()  # Get the calculated width
        height = win.winfo_height()  # Get the calculated height
        screen_width = win.winfo_screenwidth()
        screen_height = win.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        win.geometry(f"{width}x{height}+{x}+{y}")
        win.focus_force()  # Ensures the window gains focus
        site_input.focus_set()


    # ------------------------------ PASSWORD GENERATOR ------------------------------- #
    def gen_password():
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u',
                   'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
                   'P',
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

        password_input.delete(0, tkinter.END)
        password_input.insert(tkinter.END, new_password)

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
                with open("password_manager.json",
                          "r") as passwords:
                    # Reading old data
                    data = json.load(passwords)
            except FileNotFoundError:
                with open("password_manager.json",
                          "w") as passwords:
                    # Saving new data
                    json.dump(new_data, passwords, indent=4)
            else:
                # Updating old data with new data
                data.update(new_data)

                with open("password_manager.json",
                          "w") as passwords:
                    # Saving updated data
                    json.dump(data, passwords, indent=4)
            finally:
                site_input.delete(0, tkinter.END)
                password_input.delete(0, tkinter.END)
                site_input.focus()


    # ------------------------------- FIND PASSWORD ------------------------------- #
    def find_password():
        search_site = site_input.get()
        
        try:
            with open("password_manager.json", "r") as passwords:
                data = json.load(passwords)

            # Regex search for partial matches
            regex = re.compile(re.escape(search_site), re.IGNORECASE)
            matches = {key: value for key, value in data.items() if regex.search(key)}

            if not matches:
                messagebox.showerror(title="Error", message=f"No details for {search_site.title()} exist.")
                window.focus()  # Focus back to the main window
                site_input.focus_set()  # Focus back to the input field
                return

            if len(matches) == 1:
                # If there's only one match, display it directly
                website, details = next(iter(matches.items()))
                pyperclip.copy(details.get("password"))
                messagebox.showinfo(
                    title=website.title(),
                    message=f"Website: {website.title()} \n"
                            f"Email: {details.get('email')} \n"
                            f"Password: {details.get('password')}"
                )
                window.focus()  # Focus back to the main window
                site_input.focus_set()  # Focus back to the input field
            else:
                # If multiple matches are found, show a selection dialog
                def on_select(event=None):
                    if listbox.curselection():
                        selected = listbox.get(listbox.curselection())
                        details = matches[selected]
                        pyperclip.copy(details.get("password"))
                        messagebox.showinfo(
                            title=selected.title(),
                            message=f"Website: {selected.title()} \n"
                                    f"Email: {details.get('email')} \n"
                                    f"Password: {details.get('password')}"
                        )
                        selection_window.destroy()
                        window.focus()  # Focus back to the main window
                        site_input.focus_set()  # Focus back to the input field
                    else:
                        messagebox.showwarning("Selection Error", "No selection made!")
                        window.focus()  # Focus back to the main window
                        site_input.focus_set()  # Focus back to the input field

                selection_window = tkinter.Toplevel(window)
                selection_window.title("Select a Match")
                selection_window.geometry("300x200")

                tkinter.Label(selection_window, text="Select a matching website:").pack(pady=5)

                # Sort the matches alphanumerically and populate the Listbox
                sorted_matches = sorted(matches.keys(), key=lambda x: x.lower())
                listbox = tkinter.Listbox(selection_window, width=40, height=10)
                for key in sorted_matches:
                    listbox.insert(tkinter.END, key)
                listbox.pack(pady=5)

                # Bind the Return key to the selection
                listbox.bind("<Return>", on_select)

                select_button = tkinter.Button(selection_window, text="Select", command=on_select)
                select_button.pack(pady=10)

                # Automatically focus on the listbox
                listbox.focus()

        except FileNotFoundError:
            messagebox.showerror(title="Error", message="No Data File Found.")
            window.focus()  # Focus back to the main window
            site_input.focus_set()  # Focus back to the input field


    # ------------------------------ UI SETUP ------------------------------- #
    window = tkinter.Tk()
    window.title("Password Manager")
    window.config(padx=50, pady=50)

    # MyPass image
    canvas = tkinter.Canvas(width=200, height=200)
    logo_img = tkinter.PhotoImage(file="/Users/zoulaimi/Failnumbers/logo.png")
    canvas.create_image(100, 100, image=logo_img)
    canvas.grid(row=1, column=1, columnspan=3)

    # Labels
    site_label = tkinter.Label(text="Website:", justify=tkinter.RIGHT)
    site_label.grid(sticky=tkinter.E, row=2, column=1)

    email_label = tkinter.Label(text="Email/Username:", justify=tkinter.RIGHT)
    email_label.grid(sticky=tkinter.E, row=3, column=1)

    password_label = tkinter.Label(text="Password:", justify=tkinter.RIGHT)
    password_label.grid(sticky=tkinter.E, row=4, column=1)

    # Entries
    site_input = tkinter.Entry(width=22)
    site_input.grid(row=2, column=2)
    site_input.focus()
    site_input.bind("<Return>", lambda funct1: search_btn.invoke())

    email_input = tkinter.Entry(width=39)
    email_input.grid(row=3, column=2, columnspan=2)
    email_input.insert(tkinter.END, "user@email.com")
    email_input.bind("<Return>", lambda funct1: password_input.focus())

    password_input = tkinter.Entry(width=22)
    password_input.grid(row=4, column=2)

    # Buttons
    search_btn = tkinter.Button(text="Search", width=13, command=find_password)
    search_btn.grid(row=2, column=3)

    password_btn = tkinter.Button(text="Generate Password", command=gen_password)
    password_btn.grid(row=4, column=3)

    add_btn = tkinter.Button(text="Add", width=36, command=save)
    add_btn.grid(row=5, column=2, columnspan=2)

    # Center the window dynamically after adding all widgets
    center_window(window)

    window.mainloop()


if __name__ == "__main__":
    authenticate()
