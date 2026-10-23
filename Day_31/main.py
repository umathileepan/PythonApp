from tkinter import *
import random
import pandas
import time

data = pandas.read_csv("./data/french_words.csv")
to_learn = data.to_dict(orient="records") #orient give key value pair for each word
random_french_word = []

def auto_random_french_word():
    global random_french_word,flip_timer
    window.after_cancel(flip_timer)
    random_french_word = random.choice(to_learn)
    canvas.itemconfig(french_title,text="French",fill="black")
    canvas.itemconfig(french_text,text=random_french_word["French"],fill="black")
    canvas.itemconfig(canvas_back, image=front_image)
    flip_timer = window.after(3000, flip_english_card) #this will wait finishing clicking to flip in 3s


def flip_english_card():
    canvas.itemconfig(french_title,text="English",fill="white")
    canvas.itemconfig(french_text,text=random_french_word["English"],fill="white")
    canvas.itemconfig(canvas_back, image=back_image)

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")

window.configure(padx=50,pady=50,bg=BACKGROUND_COLOR)
flip_timer = window.after(3000,flip_english_card)

canvas = Canvas(width=800,height=526,background=BACKGROUND_COLOR,highlightthickness=0)
front_image = PhotoImage(file="./images/card_front.png")
back_image = PhotoImage(file="./images/card_back.png")
canvas_front = canvas.create_image(400,263,image=front_image)
canvas_back = canvas.create_image(400,263,image=back_image)
french_title = canvas.create_text(400,150,text="",font=("Arial",40,"italic"),fill="black")
french_text = canvas.create_text(400,263,text="",font=("Arial",60,"bold"),fill="black")
canvas.grid(row=0,column=0,columnspan=2)

wrong_image = PhotoImage(file="./images/wrong.png")
button_wrong = Button(image=wrong_image,highlightthickness=0,command=auto_random_french_word)
button_wrong.grid(row=1,column=0)

right_image = PhotoImage(file="./images/right.png")
button_tick = Button(image=right_image,highlightthickness=0,command=auto_random_french_word)
button_tick.grid(row=1,column=1)
auto_random_french_word()

window.mainloop()


