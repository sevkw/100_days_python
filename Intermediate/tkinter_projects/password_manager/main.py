from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

## Global Variables
FONT = ("Arial", 10)
DATA_FILE = "data.json"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
## copied from: https://replit.com/@appbrewery/password-generator-end#main.py
def generate_password():
    pswd_inpt.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]

    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)

    pswd_inpt.insert(0, password)

    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    # password = []
    website = web_input.get()
    user_addr = username_input.get()
    pswd = pswd_inpt.get()
    new_data = {
        website:{
            "email": user_addr,
            "password": pswd
            }
    }

    # password.append(website)
    # password.append(user_addr)
    # password.append(pswd)

    if len(website) == 0 or len(pswd) == 0:
        messagebox.showerror(title="Ooops!", message="Please do not leave any fields empty!😭")
    else:
        try:
            with open(DATA_FILE, "r") as data_file:
                # reading old data
                data = json.load(data_file)
                # update the old data

            with open(DATA_FILE, "w") as data_file:
                # write the updated data to the old data file
                data_file.dump(data, data_file, indent=4)
        
        except FileNotFoundError:
             with open(DATA_FILE, "w") as data_file:
                 json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
        
        finally:
            web_input.delete(0, END)
            username_input.delete(0, END)
            username_input.insert(0, "@gmail.com")
            pswd_inpt.delete(0, END)

# ---------------------------- PASSWORD SEARCH ------------------------------- #
def search_password():
    website = web_input.get()
    try:
        with open(DATA_FILE, "r") as data_file:
            data = json.load(data_file)
            email = data[website]['email']
            password = data[website]['password']
            username_input.delete(0, END)
            username_input.insert(0, email)
            pswd_inpt.insert(0, password)
    except KeyError:
        username_input.delete(0, END)
        username_input.insert(0, "@gmail.com")
        pswd_inpt.delete(0, END)
        messagebox.showerror(title="Password not found!", message="Please add the password for this website first. :)")
        

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Logo canvas
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# web label
web_label = Label(text="Website:", font=FONT)
web_label.grid(row=1, column=0)

# website inputbox
web_input = Entry(width=34)
web_input.grid(row=1, column=1)
web_input.focus()

# username  and email label
user_name = Label(text="Email/Username:", font=FONT)
user_name.grid(row=2, column=0)

# username and email inputbox
username_input = Entry(width=55)
username_input.grid(row=2, column=1, columnspan=2)
username_input.insert(0, "@gmail.com")

# pswd label
pswd_label = Label(text="Password:", font=FONT)
pswd_label.grid(row=3, column=0)

# pswd input
pswd_inpt = Entry(width=34)
pswd_inpt.grid(row=3, column=1)

# generate pswd button
pswd_button = Button(text="Generate Password", font=FONT, command=generate_password)
pswd_button.grid(row=3, column=2)

# add button
add_button = Button(text="Add Password", font=FONT, width=40, command=save)
add_button.grid(row=4, column=1, columnspan=2)

# search button
search_button = Button(text="Search", font=FONT, width=15, command=search_password)
search_button.grid(row=1, column=2)





window.mainloop()