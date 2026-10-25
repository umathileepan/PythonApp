from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self,quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20,padx=20,bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0",fg="white",bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250,bg="white")
        self.canvas.grid(row=1, column=0,columnspan=2,pady=50)

        self.question_text = self.canvas.create_text(150,125,width=280,text=self.quiz.next_question(),font=("Arial",20,"italic"),fill="black")


        self.image_tick = PhotoImage(file="./images/true.png")
        self.image_cross = PhotoImage(file="./images/false.png")
        self.button_wrong = Button(image=self.image_cross,highlightthickness=0,command=self.true_pressed)
        self.button_wrong.grid(row=2, column=0)
        self.button_correct = Button(image=self.image_tick,highlightthickness=0,command=self.false_pressed)
        self.button_correct.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz")
            self.button_correct.config(state="disabled")
            self.button_wrong.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="Red")
        self.window.after(1000, self.get_next_question)

