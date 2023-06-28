from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT = "Arial"
LEARNING_FILE = r".\data\japanese_words.csv"
TO_LEARN_FILE = r"data\words_to_learn.csv"
FLIP_AFTER_MS = 3000 ## in ms

# ----------------------------READ CSV FILE---------------------------- #
try:
    words_file = pd.read_csv(TO_LEARN_FILE)
except FileNotFoundError:
    words_file = pd.read_csv(LEARNING_FILE)

words_df = pd.DataFrame(words_file)

column_values = words_df.columns.values.tolist()
foreign_language = column_values[0]
translated_language = column_values[1]

# convert to list of dictionaries 
word_dict = words_df.to_dict(orient="records")

current_word = {}

# ---------------------------PICK RANDOM WORD ------------------------- #
def pick_word():
    global current_word, flip_timer
    # stop flipping card when this func is run
    window.after_cancel(flip_timer)
    current_word = random.choice(word_dict)
    canvas.itemconfig(word_text, text=current_word[foreign_language], fill="black")
    canvas.itemconfig(language_text, text=foreign_language, fill="black")
    canvas.itemconfig(card_bg, image=front_img)
    # need to call after when we look at the next word
    flip_timer = window.after(FLIP_AFTER_MS, flip_card)

def already_known():
    word_dict.remove(current_word)
    pd.DataFrame(word_dict).to_csv(TO_LEARN_FILE, index=False)
    pick_word()

def flip_card():
    canvas.itemconfig(card_bg, image=back_img)
    canvas.itemconfig(language_text, text=translated_language, fill="white")
    canvas.itemconfig(word_text, text=current_word[translated_language], fill="white")
    

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Japanese Flashcard")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(FLIP_AFTER_MS, flip_card)
# Card Front
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file=r".\images\card_front.png")
back_img = PhotoImage(file=r".\images\card_back.png")
card_bg = canvas.create_image(400, 263, image=front_img)
language_text = canvas.create_text(400, 150, text=foreign_language, font=(FONT, 40, 'italic'))
word_text = canvas.create_text(400, 263, text="Word", font=(FONT, 60, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)

# wrong button
wrong_img = PhotoImage(file=r".\images\wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=pick_word)
wrong_button.grid(row=1, column=0)

# yes button
yes_img = PhotoImage(file=r".\images\right.png")
yes_button = Button(image=yes_img, highlightthickness=0, command=already_known)
yes_button.grid(row=1, column=1)

pick_word()

# window.after_cancel(window)
window.mainloop()