import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk
import numpy as np  # Importing NumPy

# Create a database connection
connection = sqlite3.connect('contacts.db')
cursor = connection.cursor()

# Create the contacts table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    phone TEXT NOT NULL
)
''')
connection.commit()

# Function to add a contact
def add_contact():
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    
    if name and email and phone:
        cursor.execute("INSERT INTO contacts (name, email, phone) VALUES (?, ?, ?)", (name, email, phone))
        connection.commit()
        messagebox.showinfo("Success", "Contact added successfully!")
        name_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        display_contacts()
        count_contacts()  # Update the contact count after adding
    else:
        messagebox.showwarning("Input Error", "Please fill in all fields.")

# Function to display contacts
def display_contacts(contacts=None):
    for row in tree.get_children():
        tree.delete(row)
    
    if contacts is None:
        cursor.execute("SELECT * FROM contacts")
        contacts = cursor.fetchall()
    
    for row in contacts:
        tree.insert("", tk.END, values=row)

# Function to search contacts
def search_contacts():
    search_term = search_entry.get()
    if search_term:
        cursor.execute("SELECT * FROM contacts WHERE name LIKE ? OR email LIKE ? OR phone LIKE ?", 
                       ('%' + search_term + '%', '%' + search_term + '%', '%' + search_term + '%'))
        results = cursor.fetchall()
        display_contacts(results)
    else:
        messagebox.showwarning("Input Error", "Please enter a search term.")

# Function to count contacts
def count_contacts():
    cursor.execute("SELECT COUNT(*) FROM contacts")
    count = cursor.fetchone()[0]
    count_label.config(text=f"Total Contacts: {count}")

# Create the main window
root = tk.Tk()
root.title("Contact Manager")

# Create input fields
tk.Label(root, text="Name").grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

tk.Label(root, text="Email").grid(row=1, column=0)
email_entry = tk.Entry(root)
email_entry.grid(row=1, column=1)

tk.Label(root, text="Phone").grid(row=2, column=0)
phone_entry = tk.Entry(root)
phone_entry.grid(row=2, column=1)

# Create Add Contact button
add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.grid(row=3, columnspan=2)

# Create Search input field and button
tk.Label(root, text="Search").grid(row=4, column=0)
search_entry = tk.Entry(root)
search_entry.grid(row=4, column=1)

search_button = tk.Button(root, text="Search", command=search_contacts)
search_button.grid(row=5, columnspan=2)

# Create Treeview to display contacts
tree = ttk.Treeview(root, columns=("ID", "Name", "Email", "Phone"), show='headings')
tree.heading("ID", text="ID")
tree.heading("Name", text="Name")
tree.heading("Email", text="Email")
tree.heading("Phone", text="Phone")
tree.grid(row=6, columnspan=2)

# Create a label to display the total number of contacts
count_label = tk.Label(root, text="Total Contacts: 0")
count_label.grid(row=7, columnspan=2)

# Display existing contacts and count
display_contacts()
count_contacts()

# Close the connection when the window is closed
def on_closing():
    connection.close()  # Close the database connection
    root.destroy()      # Destroy the Tkinter window

root.protocol("WM_DELETE_WINDOW", on_closing)  # Set the closing protocol

# Start the GUI event loop
root.mainloop()