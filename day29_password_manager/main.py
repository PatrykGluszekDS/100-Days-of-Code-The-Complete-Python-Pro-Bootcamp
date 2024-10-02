from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


def find_password():
    website = website_entry.get()

    try:
        with open("passwords.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showwarning(title="Error!", message="There are no passwords in the file!")
    else:
        try:
            data_email = data[website]["email"]
            data_password = data[website]["password"]
        except KeyError:
            messagebox.showwarning(title="Error!", message="There is no such website saved.")
        else:
            messagebox.showinfo(title="Your password", message=f"Email: {data_email}\nPassword: {data_password}")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    random_letters = [choice(letters) for _ in range(randint(8, 10))]
    random_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    random_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = random_letters + random_symbols + random_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(END, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if website.strip() == "" or email.strip() == "" or password.strip() == "":
        messagebox.showwarning(title="Empty field!", message="Do not leave any empty fields!")
    else:
        try:
            with open("passwords.json", "r") as file:
                # Reading old data
                data = json.load(file)
        except FileNotFoundError:
            with open("passwords.json", "w") as file:
                # Saving updated data
                json.dump(new_data, file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("passwords.json", "w") as file:
                # Saving updated data
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry()
website_entry.focus()
website_entry.grid(column=1, row=1, sticky=EW)

email_entry = Entry()
email_entry.insert(0, "angela@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2, sticky=EW)

password_entry = Entry()
password_entry.grid(column=1, row=3, sticky=EW)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)

search_button = Button(text="Search", command=find_password)
search_button.grid(column=2, row=1, sticky=EW)

add_button = Button(text="Add", command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky=EW)

window.mainloop()
