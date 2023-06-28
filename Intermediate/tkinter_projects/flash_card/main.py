from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT = "Arial"
LEARNING_FILE = r".\data\japanese_words.csv"

# ----------------------------READ CSV FILE---------------------------- #
words_file = pd.read_csv(LEARNING_FILE)
words_df = pd.DataFrame(words_file)

column_values = words_df.columns.values.tolist()
foreign_language = column_values[0]
translated_language = column_values[1]

# convert to list of dictionaries 
jp_word_dict = words_df.to_dict(orient="records")

# ---------------------------PICK RANDOM WORD ------------------------- #
def pick_word():
    current_word = random.choice(jp_word_dict)[foreign_language]
    front_canvas.itemconfig(word_text, text=f"{current_word}")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Japanese Flashcard")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Card Front
front_canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file=r".\images\card_front.png")
front_canvas.create_image(400, 263, image=card_front_img)
front_canvas.create_text(400, 150, text=foreign_language, font=(FONT, 40, 'italic'))
word_text = front_canvas.create_text(400, 263, text="Word", font=(FONT, 60, 'bold'))
front_canvas.grid(row=0, column=0, columnspan=2)

# wrong button
wrong_img = PhotoImage(file=r".\images\wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=pick_word)
wrong_button.grid(row=1, column=0)

# yes button
yes_img = PhotoImage(file=r".\images\right.png")
yes_button = Button(image=yes_img, highlightthickness=0, command=pick_word)
yes_button.grid(row=1, column=1)

pick_word()

window.mainloop()