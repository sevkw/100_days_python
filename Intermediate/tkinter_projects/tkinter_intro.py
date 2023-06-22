import tkinter

def update_label():
    my_label.config(text=input.get())

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

#label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 20, "bold"))
my_label.pack()

# Button
button = tkinter.Button(text="Click Me", command=update_label)
button.pack()

# Entry
input = tkinter.Entry()
input.pack()








window.mainloop()