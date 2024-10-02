from tkinter import *

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)


# Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()  # expand=True, side="left"

# my_label["text"] = "New text"
# my_label.config(text="New text 2")


# Button
def button_clicked():
    print("I got clicked")
    # my_label.config(text="I got clicked")
    my_label.config(text=input.get())


button = Button(text="Click me", command=button_clicked)
button.pack()


# Entry
input = Entry(width=10)
input.insert(END, string="Some text to begin with")
input.pack()
print(input.get())


# Text
text = Text(height=5, width=30)
text.focus()  # puts cursor in textbox
text.insert(END, "Example of multi-line text entry")
print(text.get("1.0", END))  # Get's current value in textbox at line 1, character 0
text.pack()


# Spinbox
def spinbox_used():
    # gets the current value in spinbox
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# Scale
# called with current scale value
def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


# Checkbutton
def checkbutton_used():
    # Prints 1 if On button checked, otherwise 0
    print(checked_state.get())


checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()


# Radiobutton
def radio_used():
    print(radio_state.get())


# Variable to hold on to which radio button value is checked
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


# Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()


window.mainloop()
