import tkinter
from tkinter import messagebox
import random
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, 'end')
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(5, 8))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 3))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 3))]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = ''.join(password_list)
    password_entry.insert(0, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get().capitalize()
    passw = password_entry.get()
    email = email_entry.get()
    new_data = {
        website: {'password': passw, 'email': email},
    }

    if len(website) == 0 or len(passw) == 0 or len(email) == 0:
        tkinter.messagebox.showerror('Error!', 'All fields are required.')
    else:
        is_true = tkinter.messagebox.askokcancel(title='Confirm Password', message=f'Confirm the details entered: \nWebsite: {website}\nPassword: {passw}\nEmail: {email}')
        if is_true:
            try:
                with open('password_manager.json', 'r') as file:
                    old_data = json.load(file)

            except FileNotFoundError:
                with open('password_manager.json', 'w') as file:
                    json.dump(new_data, file, indent=4)
            else:
                old_data.update(new_data)

                with open('password_manager.json', 'w') as file:
                    json.dump(old_data, file, indent=4)

                tkinter.messagebox.showinfo('Success', 'Password has been saved.')
            finally:
                website_entry.delete(0, 'end')
                password_entry.delete(0, 'end')
                website_entry.focus()
# ---------------------------- SEARCH EXISTING WEBSITE DETAILS ------------------------------- #
def find_password():
    website = website_entry.get().capitalize()
    try:
        with open('password_manager.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        tkinter.messagebox.showerror('Error!', 'Password file not found.')
    else:
        if website in data:
            tkinter.messagebox.showinfo(website, f'Email: {data[website]['email']}\nPassword: {data[website]['password']}')
        else:
            tkinter.messagebox.showinfo('Error!', f'Details for {website} not found.')
# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("My Password Manager")
window.configure(padx=50, pady=50)

canvas = tkinter.Canvas(window, width=200, height=200)
image = tkinter.PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

website_label = tkinter.Label(window, text='Website: ')
website_label.grid(row=1, column=0)
name_label = tkinter.Label(window, text='Email/Username: ')
name_label.grid(row=2, column=0)
password_label = tkinter.Label(window, text='Password: ')
password_label.grid(row=3, column=0)

website_frame = tkinter.Frame(window)
website_frame.grid(row=1, column=1, columnspan=2, sticky='WE')
website_entry = tkinter.Entry(website_frame, width=24)
website_entry.pack(side='left')

email_entry = tkinter.Entry(window, width=35)
email_entry.insert(0, 'janedoe@gmail.com')
email_entry.grid(row=2, column=1, columnspan=2, sticky='WE')

passw_entry_frame = tkinter.Frame(window)
passw_entry_frame.grid(row=3, column=1, columnspan=2, sticky='WE')
password_entry = tkinter.Entry(passw_entry_frame, width=24)
password_entry.pack(side='left')

search_button = tkinter.Button(website_frame, text='Search', command=find_password)
search_button.pack(side='left', fill= 'x', expand=True)
pass_generator = tkinter.Button(passw_entry_frame, text='Generate Password', command=generate_password)
pass_generator.pack(side='left', fill='x', expand=True)
add_button = tkinter.Button(window, text='Add', width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2, sticky='W')

window.mainloop()
