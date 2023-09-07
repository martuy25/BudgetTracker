# BudgetTracker
Simple script that helps me visualizes how I spend my money
added buttons for saving and loading expenses to/from a CSV file.
integrated Matplotlib to display a pie chart representing expense categories.
Expenses are saved to a CSV file when the "Save Expenses" button is clicked, and you can load them with the "Load Expenses" button.
The pie chart is updated dynamically when expenses are added or loaded from the CSV file.
initialized the expenses DataFrame (expenses_df) to store expenses and amounts.
The Matplotlib pie chart is embedded into the tkinter GUI using FigureCanvasTkAgg.
