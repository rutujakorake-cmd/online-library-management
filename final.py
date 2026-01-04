from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__)

# Create database if not exists
def init_db():
    if not os.path.exists("library.db"):
        conn = sqlite3.connect("library.db")
        conn.execute("""
        CREATE TABLE books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL
        )
        """)
        conn.close()

def get_db_connection():
    conn = sqlite3.connect("library.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    books = conn.execute("SELECT * FROM books").fetchall()
    conn.close()
    return render_template("index.html", books=books)

@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']

        conn = get_db_connection()
        conn.execute("INSERT INTO books (title, author) VALUES (?, ?)",
                     (title, author))
        conn.commit()
        conn.close()
        return redirect('/')
    return render_template("add_book.html")

@app.route('/delete/<int:id>')
def delete_book(id):
    conn = get_db_connection()
    conn.execute("DELETE FROM books WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
