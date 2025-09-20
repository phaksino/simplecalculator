import tkinter as tk

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                result_label.config(text="Error: Division by zero")
                return
            result = num1 / num2
        else:
            result_label.config(text="Please select an operation")
            return

        result_label.config(text=f"{num1} {operation} {num2} = {result}")
    except ValueError:
        result_label.config(text="Error: Please enter valid numbers")

# Main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("320x300")

# Input fields
tk.Label(root, text="Enter first number:").pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter second number:").pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack()

# Operation selection
tk.Label(root, text="Select operation:").pack(pady=5)
operation_var = tk.StringVar(value="")

operations = [("+", "Addition"), ("-", "Subtraction"), ("*", "Multiplication"), ("/", "Division")]
for symbol, text in operations:
    tk.Radiobutton(root, text=text, variable=operation_var, value=symbol).pack(anchor="w")

# Submit button
tk.Button(root, text="Submit", command=calculate, bg="#003566", fg="white").pack(pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 14), fg="blue")
result_label.pack(pady=10)

# Run app
root.mainloop()
