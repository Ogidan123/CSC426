import tkinter as tk

def press(key):
    global expression
    if key == "C":
        expression = ""
        equation.set("")
    elif key == "=":
        try:
            result = str(eval(expression.replace("^", "**")))
            equation.set(result)
            expression = result
        except Exception:
            equation.set("Error")
            expression = ""
    else:
        expression += str(key)
        equation.set(expression)

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("350x450")
root.resizable(False, False)

expression = ""
equation = tk.StringVar()

entry = tk.Entry(root, textvariable=equation, font=("Arial", 20), justify="right", bd=10)
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=20)

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '%', '^', '+'],
    ['C', '=', '', '']
]

for r, row in enumerate(buttons, start=1):
    for c, text in enumerate(row):
        if text:
            tk.Button(
                root, text=text, font=("Arial", 16),
                width=6, height=2,
                command=lambda t=text: press(t)
            ).grid(row=r, column=c, padx=5, pady=5)

root.mainloop()
