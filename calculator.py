import tkinter as tk


calculation = ""


def calculation_string(text):
    global calculation
    textScreen.delete("1.0", tk.END)
    calculation = calculation + str(text)
    textScreen.delete("1.0", tk.END)
    textScreen.insert("1.0", calculation)


def eval_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        textScreen.delete("1.0", tk.END)
        textScreen.insert("1.0", calculation)
    except:
        textScreen.delete("1.0", tk.END)
        textScreen.insert("1.0", "Error")


def clear_field():
    global calculation
    textScreen.delete("1.0", tk.END)
    calculation = ""


root = tk.Tk()
root.geometry("300x275")
root.title("calculator")


textScreen = tk.Text(root, height=2, width=25, font=("Ariel", 16))
textScreen.grid(columnspan=5)

btnList = [1, 2, 3, "+", 4, 5, 6, "-", 7, 8, 9, "*", "(", 0, ")", "/"]

btn1 = tk.Button(
    root, text="1", width=9, height=1, command=lambda: calculation_string(1),
)
btn1.grid(row=2, column=1, pady=5)
btn2 = tk.Button(
    root, text="2", width=9, height=1, command=lambda: calculation_string(2),
)
btn2.grid(row=2, column=2, pady=5)
btn3 = tk.Button(
    root, text="3", width=9, height=1, command=lambda: calculation_string(3),
)
btn3.grid(row=2, column=3, pady=5)
btn4 = tk.Button(
    root, text="4", width=9, height=1, command=lambda: calculation_string(4),
)
btn4.grid(row=3, column=1, pady=5)
btn_plus = tk.Button(
    root, text="+", width=9, height=1, command=lambda: calculation_string("+"),
)
btn_plus.grid(row=2, column=4, pady=5)
btn5 = tk.Button(
    root, text="5", width=9, height=1, command=lambda: calculation_string(5),
)
btn5.grid(row=3, column=2, pady=5)
btn6 = tk.Button(
    root, text="6", width=9, height=1, command=lambda: calculation_string(6),
)
btn6.grid(row=3, column=3, pady=5)

btn_minus = tk.Button(
    root, text="-", width=9, height=1, command=lambda: calculation_string("-"),
)
btn_minus.grid(row=3, column=4, pady=5)


btn7 = tk.Button(
    root, text="7", width=9, height=1, command=lambda: calculation_string(7),
)
btn7.grid(row=4, column=1, pady=5)
btn8 = tk.Button(
    root, text="8", width=9, height=1, command=lambda: calculation_string(8),
)
btn8.grid(row=4, column=2, pady=5)
btn9 = tk.Button(
    root, text="9", width=9, height=1, command=lambda: calculation_string(9),
)
btn9.grid(row=4, column=3, pady=5)
btn_multiply = tk.Button(
    root, text="*", width=9, height=1, command=lambda: calculation_string("*"),
)
btn_multiply.grid(row=4, column=4, pady=5)

btnb1 = tk.Button(
    root, text="(", width=9, height=1, command=lambda: calculation_string("("),
)
btnb1.grid(row=5, column=1, pady=5)
btn0 = tk.Button(
    root, text="0", width=9, height=1, command=lambda: calculation_string(0),
)
btn0.grid(row=5, column=2, pady=5)
btnb2 = tk.Button(
    root, text=")", width=9, height=1, command=lambda: calculation_string(")"),
)
btnb2.grid(row=5, column=3, pady=5)
btn_division = tk.Button(
    root, text="/", width=9, height=1, command=lambda: calculation_string("/"),
)
btn_division.grid(row=5, column=4, pady=5)


btn_clear = tk.Button(root, text="C", width=18, height=2, command=clear_field)
btn_clear.grid(row=6, column=1, columnspan=2)
btn_evaluate = tk.Button(root, text="=", width=18, height=2, command=eval_calculation)
btn_evaluate.grid(row=6, column=3, columnspan=2)

root.mainloop()

