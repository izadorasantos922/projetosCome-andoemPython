from tkinter import *

def calculate():
    miles = float(miles_input.get())
    km = miles * 1.60934
    kilometer_result_label.config(text=f"{km:.2f}")

window = Tk()
window.title("Mile to KM")
window.config(padx=50, pady=50) 

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=2)

for widget in window.grid_slaves():
    widget.grid_configure(padx=10, pady=10)

window.mainloop()
