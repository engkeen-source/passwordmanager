from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
from pyperclip import copy
import json

TITLE = 'Password Manager'


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter = [choice(letters) for _ in range(randint(8, 10))]
    symbol = [choice(symbols) for _ in range(randint(2, 4))]
    number = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = letter + symbol + number
    shuffle(password_list)

    password = ''.join(password_list)
    password_input.insert(0, password)
    copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input.get()
    credential_id = id_input.get()
    credential_password = password_input.get()
    new_data = {
        website: {
            'email': credential_id,
            'password': credential_password
        }
    }

    if len(website) == 0 or len(credential_id) == 0 or len(credential_password) == 0:
        messagebox.showerror(title='Oops', message="Please don't leave any field empty.")

    is_ok = messagebox.askokcancel(title=website, message=f"There are the details entered: \nEmail: {credential_id}"
                                                          f"\nPassword: {credential_password} \nIs it ok to save")
    if is_ok:
        try:
            with open('data.json', 'r') as data_file:
                data = json.load(data_file)
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, 'end')
            id_input.delete(0, 'end')
            password_input.delete(0, 'end')


def find_password():
    website = website_input.get()
    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title='Oops', message="No data file found.")
    else:
        # Look for password object
        credential_id = data[website]['email']
        credential_password = data[website]['password']
        messagebox.showinfo(title='Retrieve success', message=f"Website: {website} \nEmail: {credential_id}"
                                                              f"\nPassword: {credential_password}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title(TITLE)
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Label
website_label = Label(text='Website:')
website_label.grid(column=0, row=1)
id_label = Label(text='Email/Username:')
id_label.grid(column=0, row=2)
password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

# Entries
website_input = Entry(width=21)
website_input.grid(column=1, row=1)
id_input = Entry(width=39)
id_input.grid(column=1, row=2, columnspan=2)
password_input = Entry(width=21)
password_input.grid(column=1, row=3)

# Buttons
generate_password_button = Button(text='Generate Password', command=generate_password)
generate_password_button.grid(column=2, row=3)
add_object_button = Button(text='Add', width=33, command=save_password)
add_object_button.grid(column=1, row=4, columnspan=2)
search_button = Button(text='Search', width=13, command=find_password)
search_button.grid(column=2, row=1)

window.mainloop()
