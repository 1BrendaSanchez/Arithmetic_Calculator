import tkinter as tk

window = tk.Tk()
window.geometry("600x300")
window.title("Calculator App")

# creating the widgets
num1 = tk.Label(text="Enter 1st Number: ")
num1.grid(column=0, row=0)
num1Entry = tk.Entry()
num1Entry.grid(column=1, row=0)

num2 = tk.Label(text="Enter 2nd Number: ")
num2.grid(column=0, row=1)
num2Entry = tk.Entry()
num2Entry.grid(column=1, row=1)


# button event method

def addNumbers():
    a = int(num1Entry.get())
    b = int(num2Entry.get())
    s = a + b
    result = "The sum is {0}".format(s)
    textArea = tk.Text(master=window, height=7, width=15)
    textArea.grid(column=1, row=3)
    textArea.insert(tk.END, result)


button = tk.Button(window, text="Calculate Sum", command=addNumbers, bg="lightgreen")
button.grid(column=1, row=2)

window.mainloop()
