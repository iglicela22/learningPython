from flask import Flask, render_template, request, redirect, url_for
from livereload import Server
import sqlite3

app = Flask(__name__)
DB_NAME = "todo.db"

# Initialize database
def init_db():
    print("Initializing database...")
    conn = sqlite3.connect(DB_NAME)
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL,
            list_name TEXT NOT NULL DEFAULT 'General',
            completed INTEGER NOT NULL DEFAULT 0
        )
        """
    )
    conn.commit()
    conn.close()

init_db()

# Database connection helper
def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

# Delete a task
@app.route("/delete/<int:id>", methods=["GET"])
def delete(id):
    conn = get_db_connection()
    conn.execute("DELETE FROM tasks WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect("/")

# Complete a task (marks as done and moves to "Done" list)
@app.route("/complete/<int:id>", methods=["POST"])
def complete(id):
    conn = get_db_connection()
    conn.execute(
        "UPDATE tasks SET completed = 1, list_name = 'Done' WHERE id = ?",
        (id,)
    )
    conn.commit()
    conn.close()
    return redirect(url_for("home"))

# Main page (view/add tasks)
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        task_content = request.form.get("content")
        list_name = request.form.get("list_name", "General")

        if task_content and task_content.strip():
            conn = get_db_connection()
            conn.execute(
                "INSERT INTO tasks (content, list_name) VALUES (?, ?)",
                (task_content.strip(), list_name)
            )
            conn.commit()
            conn.close()
        return redirect(url_for("home"))

    conn = get_db_connection()
    tasks = conn.execute("SELECT * FROM tasks").fetchall()
    conn.close()
    return render_template("index.html", tasks=tasks)

# Run with livereload
if __name__ == "__main__":
    server = Server(app.wsgi_app)
    server.watch('templates/*.html')
    server.watch('static/*.css')
    server.serve(port=5000, host='127.0.0.1', debug=True)
