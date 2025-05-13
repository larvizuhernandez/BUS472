import tkinter as tk  # Import the main Tkinter module for GUI development
from tkinter import ttk, messagebox  # Import ttk for advanced widgets and messagebox for alert dialogs
from datetime import datetime  # Import datetime to add a timestamp to each expense

# Global list to store expense records
expenses = []


def add_expense():
    # Retrieve data from the GUI input fields
    desc = desc_entry.get()  # Get the expense description
    amount_text = amount_entry.get()  # Get the entered amount as text
    category = category_var.get()  # Get the selected expense category

    payment = payment_var.get() # allows user to select payment method used
    if not desc or not amount_text:
        messagebox.showerror("Input Error", "Please fill in both description and amount.")
        return
    try:
        amount = float(amount_text)  # Convert amount to a float for calculations
    except ValueError:
        messagebox.showerror("Input Error", "Amount must be a number.")
        return
    date_str = datetime.now().strftime("%Y-%m-%d")  # Get the current date formatted as YYYY-MM-DD

    # Create a record for the expense and add it to the list
    expenses.append({"date": date_str, "desc": desc, "amount": amount, "category": category, "payment": payment})

    # Insert the expense record into the treeview table
    tree.insert("", tk.END, values=(date_str, desc, f"${amount:.2f}", category, payment))

    # Clear the entry fields after adding the expense
    desc_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)

    # Update the total expense displayed in the GUI
    update_total()


def update_total():
    # Calculate the total expenses by summing the amounts of each record in the list
    total = sum(exp["amount"] for exp in expenses)
    total_label.config(text=f"Total Expense: ${total:.2f}")


def clear_expenses():
    # Clear the global list of expenses and the treeview display
    global expenses
    expenses = []
    for item in tree.get_children():
        tree.delete(item)
    update_total()


# -------------------------- GUI Setup --------------------------
app = tk.Tk()  # Create the main application window
app.title("Expense Tracker")  # Set the window title
app.geometry("1000x600")  # Set the window size (width x height)

# Frame for input fields to add a new expense
input_frame = tk.Frame(app)
input_frame.pack(pady=10)  # .pack() places the frame with padding of 10 pixels vertically

# Label and entry for expense description
desc_label = tk.Label(input_frame, text="Expense Description:")
desc_label.grid(row=0, column=0, padx=5, pady=5,
                sticky="e")  # .grid() organizes the label in the first row, first column with padding
desc_entry = tk.Entry(input_frame, width=30)
desc_entry.grid(row=0, column=1, padx=5, pady=5)

# Label and entry for the expense amount
amount_label = tk.Label(input_frame, text="Amount:")
amount_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
amount_entry = tk.Entry(input_frame, width=30)
amount_entry.grid(row=1, column=1, padx=5, pady=5)

# Label and dropdown for selecting expense category
category_label = tk.Label(input_frame, text="Category:")
category_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
category_var = tk.StringVar(value="Others")  # Default category value
category_options = ["Food", "Transport", "Shopping", "Bills", "Others"]
category_menu = tk.OptionMenu(input_frame, category_var, *category_options)
category_menu.grid(row=2, column=1, padx=5, pady=5, sticky="w")

#Lable with dropdown that allows user to select payment type
payment_label = tk.Label(input_frame, text="Payment Type")
payment_label.grid(row=3, column=0, padx=5, pady=5, sticky="e")
payment_var = tk.StringVar(value="Cash")
payment_options = ["Cash", "Credit Card", "Debit Card", "Other"]
payment_menu = tk.OptionMenu(input_frame, payment_var, *payment_options)
payment_menu.grid(row=3, column=1, padx=5, pady=5, sticky="w")

# Button to add an expense record
add_button = tk.Button(app, text="Add Expense", command=add_expense)
add_button.pack(pady=5)

# Treeview widget to display the list of expenses in a table format
columns = ("Date", "Description", "Amount", "Category", "Payment")
tree = ttk.Treeview(app, columns=columns, show="headings", height=10)
for col in columns:
    tree.heading(col, text=col)  # Set the heading text for each column
    tree.column(col, anchor="center")  # Center align each column
tree.pack(pady=10)

# Label to display the total expense amount
total_label = tk.Label(app, text="Total Expense: $0.00", font=("Arial", 12, "bold"))
total_label.pack(pady=5)

# Button to clear all expense records from the tracker
clear_button = tk.Button(app, text="Clear All Expenses", command=clear_expenses)
clear_button.pack(pady=5)

# Start the Tkinter event loop
app.mainloop()
