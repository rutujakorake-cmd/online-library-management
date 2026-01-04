import tkinter as tk
from tkinter import messagebox, simpledialog

# ------------------------------
# Library Data
# ------------------------------
library = [
    {"id": 1, "title": "Python Basics", "author": "John Smith", "available": True},
    {"id": 2, "title": "Data Science 101", "author": "Jane Doe", "available": True},
    {"id": 3, "title": "AI for Beginners", "author": "Elon Ray", "available": True},
]

borrowed_books = {}  # student → book title mapping


# ------------------------------
# Display Books
# ------------------------------
def display_books():
    listbox.delete(0, tk.END)
    for book in library:
        status = "Available" if book["available"] else "Issued"
        listbox.insert(tk.END, f"{book['id']} - {book['title']} - {book['author']} - {status}")


# ------------------------------
# Issue Book
# ------------------------------
def issue_book():
    try:
        student = simpledialog.askstring("Student Name", "Enter student name:")
        book_id = int(simpledialog.askstring("Book ID", "Enter Book ID to issue:"))

        for book in library:
            if book["id"] == book_id:
                if book["available"]:
                    book["available"] = False
                    borrowed_books[student] = book["title"]
                    messagebox.showinfo("Success", f"Book '{book['title']}' issued to {student}.")
                    display_books()
                    return
                else:
                    messagebox.showerror("Unavailable", "This book is already issued.")
                    return
        messagebox.showerror("Not Found", "Book not found!")
    except:
        messagebox.showerror("Invalid", "Invalid Book ID.")


# ------------------------------
# Return Book
# ------------------------------
def return_book():
    student = simpledialog.askstring("Student Name", "Enter student name:")

    if student in borrowed_books:
        book_title = borrowed_books.pop(student)

        for book in library:
            if book["title"] == book_title:
                book["available"] = True
                messagebox.showinfo("Returned", f"Book '{book_title}' returned successfully.")
                display_books()
                return
    else:
        messagebox.showerror("Not Found", "No record found for this student.")


# ------------------------------
# Add Book
# ------------------------------
def add_book():
    try:
        book_id = int(simpledialog.askstring("Book ID", "Enter new Book ID:"))
        title = simpledialog.askstring("Title", "Enter Book Title:")
        author = simpledialog.askstring("Author", "Enter Author Name:")

        library.append({"id": book_id, "title": title, "author": author, "available": True})
        messagebox.showinfo("Added", f"Book '{title}' added successfully.")
        display_books()
    except:
        messagebox.showerror("Error", "Book ID must be a number!")


# ------------------------------
# Search Book
# ------------------------------
def search_book():
    keyword = simpledialog.askstring("Search", "Enter title or author keyword:").lower()
    listbox.delete(0, tk.END)
    found = False

    for book in library:
        if keyword in book["title"].lower() or keyword in book["author"].lower():
            listbox.insert(tk.END, f"Found: {book['title']} by {book['author']}")
            found = True
    
    if not found:
        messagebox.showinfo("Not Found", "No matching books found.")


# ------------------------------
# GUI Window
# ------------------------------
root = tk.Tk()
root.title("Library Management System")
root.geometry("600x400")

# Title Label
title_label = tk.Label(root, text="Library Management System", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Books List
listbox = tk.Listbox(root, width=80, height=12)
listbox.pack(pady=10)

display_books()

# Buttons Frame
frame = tk.Frame(root)
frame.pack()

tk.Button(frame, text="Display Books", width=15, command=display_books).grid(row=0, column=0, padx=5, pady=5)
tk.Button(frame, text="Issue Book", width=15, command=issue_book).grid(row=0, column=1, padx=5, pady=5)
tk.Button(frame, text="Return Book", width=15, command=return_book).grid(row=0, column=2, padx=5, pady=5)
tk.Button(frame, text="Add Book", width=15, command=add_book).grid(row=1, column=0, padx=5, pady=5)
tk.Button(frame, text="Search Book", width=15, command=search_book).grid(row=1, column=1, padx=5, pady=5)
tk.Button(frame, text="Exit", width=15, command=root.quit).grid(row=1, column=2, padx=5, pady=5)

root.mainloop()
