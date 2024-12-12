# Password Manager with Authentication

## Overview

This project is a **Password Manager** application built using Python and the `tkinter` library. It provides functionality for securely managing passwords, including generating, storing, and searching passwords. The application also includes user authentication to ensure only authorized users can access the password manager.

---

## Features

### **Authentication**

- Users are required to enter a master password to access the application.
- The password entry is validated, and incorrect entries result in an error message.
- User interaction is secured by clearing the input field after an incorrect entry.

### **Password Management**

- **Add Passwords**: Save website credentials (website, email, and password).
- **Search Passwords**: Retrieve credentials for specific websites.
  - Partial matches are supported using **fuzzy search** with regular expressions.
  - Results are displayed dynamically in a Listbox for user selection.
- **Password Generation**: Generate strong, random passwords with a mix of letters, numbers, and symbols. The generated password is copied to the clipboard for convenience.

### **Dynamic UI Enhancements**

- Fully interactive user interface built with `tkinter`.
- Dynamic centering of application windows for improved usability.
- Listbox integration for displaying multiple search results with selection functionality.
- Error handling and clear feedback to users.

---

## Requirements

### **Python Version**

- Python 3.8 or above

### **Dependencies**

Install the following libraries if not already available:

- `tkinter` (standard library for Python GUIs)
- `pyperclip` (for clipboard functionality)
- `re` (regular expressions for fuzzy search)
- `json` (for data storage and retrieval)

Install missing libraries using:

```bash
pip install pyperclip
```

---

## File Structure

- **main.py**: The main application file containing all logic.
- **password_manager.json**: JSON file for storing password data (created automatically).
- **logo.png**: Placeholder logo image displayed in the application.

---

## How to Run

1. Clone the repository or copy the project files to your local machine.
2. Ensure all dependencies are installed.
3. Run the program:
   ```bash
   python main.py
   ```
4. Enter the master password (`admin1234` by default) to access the password manager.

---

## Usage

### **Authentication**

1. Launch the application.
2. Enter the master password in the login window.
3. Press `Enter` or click the `Login` button.

### **Changing the Master Password**

To change the master password, edit the `MASTER_PASSWORD` variable in the `authenticate` function in `main.py`.

### **Adding a Password**

1. Enter the website name, email/username, and password in the respective fields.
2. Click the `Add` button to save the credentials.
3. The data is stored in `password_manager.json`.

### **Generating a Password**

1. Leave the "Password" field empty and click the `Generate Password` button.
2. The generated password will be automatically inserted into the password field and copied to the clipboard.

### **Searching for a Password**

1. Enter the website name in the "Website" field.
2. Click the `Search` button.
3. If a match is found:
   - If a single match exists, the details are displayed directly.
   - If multiple matches are found, a Listbox appears for selection. Select a match and press `Enter` to view its details.

---

## Security Notes

- The master password is hardcoded as `admin1234`. Change this value in the `authenticate` function to secure your application.
- Password data is stored in plaintext JSON format. For enhanced security, consider encrypting the file using libraries like `cryptography`.

---

## Future Improvements

- Add user-specific authentication and registration.
- Encrypt stored passwords using a secure encryption algorithm.
- Allow users to update or delete existing credentials.
- Add multi-platform support and a more modern UI framework (e.g., PyQt or Tkinter ttk).

---

## Author

Based on an original concept sourced externally and expanded significantly by **Zoulaimi**. This version includes enhanced features such as authentication, fuzzy search, dynamic Listbox integration, and improved user interaction.
