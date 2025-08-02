from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
DB_FILE = "bookshelf.db"

def init_db():
    with sqlite3.connect(DB_FILE) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL
            )
        """)

@app.route("/books", methods=["GET"])
def list_books():
    with sqlite3.connect(DB_FILE) as conn:
        books = conn.execute("SELECT title, author FROM books").fetchall()
    return jsonify([{"title": t, "author": a} for t, a in books])

@app.route("/books", methods=["POST"])
def add_book():
    data = request.json
    with sqlite3.connect(DB_FILE) as conn:
        conn.execute("INSERT INTO books (title, author) VALUES (?, ?)", (data["title"], data["author"]))
    return {"message": "Book added"}, 201

@app.route("/books/<title>", methods=["DELETE"])
def delete_book(title):
    with sqlite3.connect(DB_FILE) as conn:
        conn.execute("DELETE FROM books WHERE title = ?", (title,))
    return {"message": "Book removed"}, 200

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=8080)
