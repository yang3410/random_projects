# -*- coding: utf-8 -*-
"""
Created on Tue Aug 12 14:54:21 2025

@author: 

 - prediction calculation trigger when data marked as first day is entered
 - 


    
"""

import tkinter as tk
from tkinter import messagebox
import json
import os

DATA_FILE = "records.json"

# Load existing data if file exists
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

# Save data to file
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# Handle record submission
def add_record():
    name = entry_name.get().strip()
    age = entry_age.get().strip()

    if not name or not age:
        messagebox.showwarning("Missing Data", "Please fill in all fields.")
        return

    try:
        age_int = int(age)
    except ValueError:
        messagebox.showwarning("Invalid Input", "Age must be a number.")
        return

    data.append({"name": name, "age": age_int})
    save_data(data)

    # Clear fields
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)

    messagebox.showinfo("Success", f"Record saved for {name}.")

# Show saved records
def show_records():
    records_text.delete("1.0", tk.END)
    for idx, record in enumerate(data, start=1):
        records_text.insert(tk.END, f"{idx}. {record['name']} - {record['age']} years\n")

# UI setup
root = tk.Tk()
root.title("Data Recording App")

tk.Label(root, text="Name:").grid(row=0, column=0, padx=5, pady=5)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Age:").grid(row=1, column=0, padx=5, pady=5)
entry_age = tk.Entry(root)
entry_age.grid(row=1, column=1, padx=5, pady=5)

btn_add = tk.Button(root, text="Add Record", command=add_record)
btn_add.grid(row=2, column=0, columnspan=2, pady=10)

btn_show = tk.Button(root, text="Show Records", command=show_records)
btn_show.grid(row=3, column=0, columnspan=2, pady=5)

records_text = tk.Text(root, width=40, height=10)
records_text.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

data = load_data()

root.mainloop()
