# link to Angela Yu's answer: https://www.udemy.com/course/100-days-of-code/learn/lecture/20781174


from tkinter import *

FONT = ("Arial", 12, "normal")

def mile_to_km():
    miles = float(mile_input.get())
    km = round(miles * 1.60934, 2)
    converted_label.config(text=f"{km}")

# GUI Window
window = Tk()
window.title("Mile to KM Converter")
window.minsize(width=240, height=120)
window.config(padx=10, pady=20)


# miles entry box
mile_input = Entry(width=10)
mile_input.insert(END, string="0")
mile_input.grid(column=1, row=0)

# miles label
mile_label = Label(text="Miles", font=FONT)
mile_label.grid(column=2, row=0)

# converted labels
equal_to_label = Label(text="is equal to", font=FONT)
equal_to_label.grid(column=0, row=1)

# converted_km label
converted_label = Label(text="0", font=FONT)
converted_label.grid(column=1, row=1)

# km label
km_label = Label(text="KM", font=FONT)
km_label.grid(column=2, row=1)

# calculate button
calculate_button = Button(text="Calculate", command=mile_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()