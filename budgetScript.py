import tkinter as tk
from tkinter import messagebox
import pygal
from pygal.style import Style
import webbrowser

#function to handle "add expense" button
def add_expense():
    expense = entry_expense.get()
    amount = entry_amount.get()
    
    if expense and amount:
        #add expenses to listbox
        listbox_expenses.insert(tk.END, f"{expense}: ${amount}")
        
        #update total
        current_budget = float(label_budget.cget("text"))
        current_budget-= float(amount)
        label_budget.config(text=str(current_budget))
        
        #clear input fields
        entry_expense.delete(0,tk.END)
        entry_amount.delete(0,tk.END)
    else:
        messagebox.showwarning('Missing Information', "Please enter both expense and amount.")

def generate_chart():
    chart = pygal.Pie(Style=custom_style)
    for item in listbox_expenses.get(0,tk.END):
        expense, amount = item.split(': $')
        chart.add(expense, float(amount))
        
    chart.render_to_file("budget_chart.svg")
    chart_url = "budget_chart.svg"
    
    #open chart in web browser
    webbrowser.open(chart_url, new=2)
    
#main app window
app =tk.Tk()
app.title("Budget Tracker")

#widget creation
label_budget = tk.Label(app, text="$1000.00", font=("Arial", 14))
label_budget.pack(pady=10)
frame_add_expense = tk.Frame(app)
frame_add_expense.pack(padx=10,pady=10)
label_expense = tk.Label(frame_add_expense, text="Expense:")
label_expense.grid(row=0, column=0)
entry_expense = tk.Entry(frame_add_expense)
entry_expense.grid(row=0, column=1)
label_amount = tk.Label(frame_add_expense, text="Amount:")
label_amount.grid(row=1, column=0)
entry_amount = tk.Entry(frame_add_expense)
entry_amount.grid(row=1, column=1)
button_add = tk.Button(frame_add_expense, text="Add Expense", command=add_expense)
button_add.grid(row=2, columnspan=2)
listbox_expenses = tk.Listbox(app)
listbox_expenses.pack(padx=10, pady=10)
button_generate_chart = tk.Button(app, text="Generate Chart", command=generate_chart)
button_generate_chart.pack(pady=10)

initial_budget =1000.00
label_budget.config(text=str(initial_budget))

custom_style = Style(
    background = 'transparent',
    title_font_size=20,
    label_font_size=16,
)

app.mainloop()


