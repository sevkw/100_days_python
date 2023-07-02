from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = "Arial"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)

        self.quiz_text = self.canvas.create_text(
            150,
            125,
            ## this width parameter will wrap long text
            width=280,
            text="Quiz Text",
            font=(FONT, 16, "italic"),
            fill="black"
        )
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=50)

        self.score_label = Label(text="Score: ", font=(FONT,10, "bold"), bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        check_img = PhotoImage(file=r".\images\true.png")
        cross_img = PhotoImage(file=r".\images\false.png")
        self.true_button = Button(image=check_img, highlightthickness=0, command=self.validate_true_button)
        self.true_button.grid(row=2, column=0, padx=20, pady=20)
        self.false_button = Button(image=cross_img, highlightthickness=0, command=self.validate_false_button)
        self.false_button.grid(row=2, column=1, padx=20, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.configure(bg="white")
        if self.quiz_brain.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz_brain.score}")
            q_text = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.quiz_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.quiz_text,
                text="You have reached the end of the quiz!"
            )
            # disable button press
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    
    def validate_true_button(self):
        self.give_feedback(
            self.quiz_brain.check_answer('True')
        )      
    
    def validate_false_button(self):
        self.give_feedback(
            self.quiz_brain.check_answer('False'))
    
    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")
        self.window.after(
            1000,
            self.get_next_question
        )