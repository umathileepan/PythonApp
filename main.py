from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = input_website.get()
    email = input_email.get()
    password = input_password.get()
    with open("data.txt",mode="w") as file:
        file.write(website + " | " + email + " | " + password + "\n")
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
input_website = Entry(width=35)
input_website.focus()
input_website.grid(row=1,column=1,columnspan=2)

label_email = Label(text="Email/Username:")
label_email.grid(row=2,column=0)
input_email = Entry(width=35)
input_email.insert(0,"umathileepan@gmail.com")
input_email.grid(row=2,column=1,columnspan=2)

label_password = Label(text="Password:")
label_password.grid(row=3,column=0)
input_password = Entry(width=21)
input_password.grid(row=3,column=1)

button_generate_password = Button(text="Generate Password")
button_generate_password.grid(row=3,column=2)

button_add = Button(text="Add",width=35,command=save_password)
button_add.grid(row=4,column=0,columnspan=3)


window.mainloop()