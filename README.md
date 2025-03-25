Database Setup:

The code establishes a connection to a SQLite database named contacts.db.
It creates a table called contacts with columns for id, name, email, and phone if it doesn't already exist.
GUI Setup:

The main window is created using tkinter, with a title "Contact Manager".
Input fields are provided for the user to enter contact details: name, email, and phone number.
Buttons are included for adding contacts and searching for contacts.
Functions:

add_contact(): This function retrieves the input from the user, checks if all fields are filled, and inserts the new contact into the database. It also updates the displayed contacts and the total count.
display_contacts(): This function fetches all contacts from the database and displays them in a Treeview widget.
search_contacts(): This function allows users to search for contacts by name, email, or phone number. It updates the displayed contacts based on the search term.
count_contacts(): This function counts the total number of contacts in the database and updates a label displaying this count.
User Interface Elements:

Labels and entry fields for user input.
A Treeview widget to display the list of contacts in a tabular format.
A label to show the total number of contacts.
Closing Protocol:

The application ensures that the database connection is closed when the window is closed by implementing the on_closing() function.
Event Loop:
Technologies used:
Programming Language: Python
Database: SQLite (via the sqlite3 module)
GUI Toolkit: Tkinter (with ttk for themed widgets)
Optional Library: NumPy (not used in the current implementation)

Potential Enhancements
Delete Functionality: Allow users to delete contacts.
Edit Functionality: Enable users to edit existing contact details.
Additional Fields: Include more fields such as address, age, or salary.
Improved Search: Implement more advanced search options or filters.
Data Validation: Add validation for email formats and phone numbers.
