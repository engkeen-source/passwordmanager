from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
from pyperclip import copy

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

    if len(website) == 0 or len(credential_id) == 0 or len(credential_password) == 0:
        messagebox.showerror(title='Oops', message="Please don't leave any field empty.")

    is_ok = messagebox.askokcancel(title=website, message=f"There are the details entered: \nEmail: {credential_id}"
                                   f"\nPassword: {credential_password} \nIs it ok to save")
    if is_ok:
        with open("data.txt", "a") as f:
            f.write(f"{website} | {credential_id} | {credential_password}\n")
            website_input.delete(0, 'end')
            id_input.delete(0, 'end')
            password_input.delete(0, 'end')


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
website_input = Entry(width=39)
website_input.grid(column=1, row=1, columnspan=2)
id_input = Entry(width=39)
id_input.grid(column=1, row=2, columnspan=2)
password_input = Entry(width=21)
password_input.grid(column=1, row=3)

# Buttons
generate_password_button = Button(text='Generate Password', command=generate_password)
generate_password_button.grid(column=2, row=3)
add_object_button = Button(text='Add', width=33, command=save_password)
add_object_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
