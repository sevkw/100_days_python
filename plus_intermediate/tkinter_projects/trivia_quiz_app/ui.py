from tkinter import *

THEME_COLOR = "#375362"
FONT = "Arial"


class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)

        self.quiz_text = self.canvas.create_text(150, 125, text="Quiz Text", font=(FONT, 16, "italic"), fill="black")
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

        self.label = Label(text="Score: ", font=(FONT,10, "bold"), bg=THEME_COLOR, fg="white")
        self.label.grid(row=0, column=1)

        self.check_img = PhotoImage(file=r".\images\true.png")
        self.cross_img = PhotoImage(file=r".\images\false.png")
        self.tick_button = Button(image=self.check_img, highlightthickness=0)
        self.tick_button.grid(row=2, column=0, padx=20, pady=20)
        self.cross_button = Button(image=self.cross_img, highlightthickness=0)
        self.cross_button.grid(row=2, column=1, padx=20, pady=20)






        self.window.mainloop()