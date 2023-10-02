import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.result_var = tk.StringVar()

        # Entry to display the expression and result
        self.entry = tk.Entry(root, textvariable=self.result_var, font=("Arial", 24), bd=10, insertwidth=2, width=15, justify='right')
        self.entry.grid(row=0, column=0, columnspan=4)

        # Button layout
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        for (text, row, column) in buttons:
            button = tk.Button(root, text=text, font=("Arial", 18), padx=20, pady=20, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=column)

    def on_button_click(self, char):
        if char == '=':
            try:
                result = eval(self.result_var.get())
                self.result_var.set(str(result))
            except:
                self.result_var.set('Error')
        else:
            current_expression = self.result_var.get()
            new_expression = current_expression + char
            self.result_var.set(new_expression)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = CalculatorApp(root)
    root.mainloop()
