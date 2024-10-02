from tkinter import *

FONT = ("Arial", 12, "bold")


def button_command():
    miles_number = int(entry.get())
    km_number = int(round(1.6*miles_number, 0))
    result.config(text=f"{km_number}")


window = Tk()
window.title("Mile to km converter")
window.config(padx=20, pady=20)

# "miles" label
miles = Label(text="miles", font=FONT)
miles.grid(column=2, row=0)

# "is equal to" label
is_equal_to = Label(text="is equal to", font=FONT)
is_equal_to.grid(column=0, row=1)

# result label
result = Label(text="0", font=FONT)
result.grid(column=1, row=1)

# "km" label
km = Label(text='km', font=FONT)
km.grid(column=2, row=1)


# Entry label
entry = Entry()
entry.grid(column=1, row=0)


# Button label
calculate = Button(text="Calculate", command=button_command)
calculate.grid(column=1, row=2)


window.mainloop()
