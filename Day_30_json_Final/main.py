from tkinter import * #here import all of the classes in the tkinter
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters =[random.choice(letters) for _ in range(nr_letters)]
    #for char in range(nr_letters):
      #password_list.append(random.choice(letters))

    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    #for char in range(nr_symbols):
      #password_list += random.choice(symbols)

    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    #for char in range(nr_numbers):
     # password_list += random.choice(numbers)
    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    #password = ""
    #for char in password_list:
     # password += char
    input_password.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = input_website.get()
    email = input_email.get()
    password = input_password.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving update data
                json.dump(data, data_file, indent=4)
        finally:
            input_website.delete(0, END)
            input_password.delete(0, END)


def search():
    website = input_website.get()
    try:
        with open("data.json", "r") as data_file:
            # Reading old data
            data = json.load(data_file)
    except FileNotFoundError:
         messagebox.showinfo(title="Error", message="No data file found.")
    else:
        if website in data:
            messagebox.showinfo(title="Website", message=f"Email: {data[website]['email']}\n Password: {data[website]['password']}")
        else:
            messagebox.showinfo(title="Error",message="Website not in there")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200,height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_image)
canvas.grid(row=0,column=1)

label_website = Label(text="Website:")
label_website.grid(row=1,column=0)
input_website = Entry(width=32)
input_website.focus()
input_website.grid(row=1,column=1)
button_search = Button(text="Search",width=15,command=search)
button_search.grid(row=1,column=2)

label_email = Label(text="Email/Username:")
label_email.grid(row=2,column=0)
input_email = Entry(width=52)
input_email.insert(0,"umathileepan@gmail.com")
input_email.grid(row=2,column=1,columnspan=2)

label_password = Label(text="Password:")
label_password.grid(row=3,column=0)
input_password = Entry(width=32)
input_password.grid(row=3,column=1)

button_generate_password = Button(text="Generate Password",command=generate_password)
button_generate_password.grid(row=3,column=2)

button_add = Button(text="Add",width=44,command=save_password)
button_add.grid(row=4,column=1,columnspan=2)


window.mainloop()