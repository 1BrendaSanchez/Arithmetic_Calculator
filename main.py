import tkinter as tk

window = tk.Tk()
window.geometry("600x300")
window.title("Calculator App")

num1 = tk.Label(text="Enter 1st Number: ")
num1.grid(column=0, row=0)
num1Entry = tk.Entry()
num1Entry.grid(column=1, row=0)

num2 = tk.Label(text="Enter 2nd Number: ")
num2.grid(column=0, row=1)
num2Entry = tk.Entry()
num2Entry.grid(column=1, row=1)

button = tk.Button(window, text="Calculate Sum")
button.grid(column=1, row=2)

window.mainloop()
