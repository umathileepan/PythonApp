from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
#window.minsize(400, 400)
window.configure(padx=20,pady=20,bg=BACKGROUND_COLOR)

canvas = Canvas(width=570,height=400,background=BACKGROUND_COLOR)
front_image = PhotoImage(file="./images/card_front.png")
back_image = PhotoImage(file="./images/card_back.png")
canvas.create_image(200,200,image=front_image)
canvas.grid(row=0,column=0,columnspan=2)

wrong_image = PhotoImage(file="./images/wrong.png")
button_wrong = Button(image=wrong_image,highlightthickness=0)
button_wrong.grid(row=1,column=0)

right_image = PhotoImage(file="./images/right.png")
button_tick = Button(image=right_image,highlightthickness=0)
button_tick.grid(row=1,column=1)


window.mainloop()


