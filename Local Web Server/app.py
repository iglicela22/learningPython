from flask import Flask, render_template, request, redirect, url_for 
from datetime import datetime
import sqlite3

app = Flask(__name__)
DB_NAME = "todo.db"


def init_db():
    print("Initializing database...")
    conn = sqlite3.connect(DB_NAME)
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL,
            list_name TEXT NOT NULL DEFAULT 'General',   -- <-- Add comma here
            completed INTEGER NOT NULL DEFAULT 0         -- <-- 0 = not done, 1 = done
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,  -- <-- Add created_at column
            
        )
        """
    )
    conn.commit()
    conn.close()


# Ensure the database is initialized when the app starts
init_db()


def get_db_connection():
    """Create and return a new database connection with row access by column name."""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/delete/<int:id>", methods=["GET"])
def delete(id):
    """Delete a task by its ID and redirect to the homepage."""
    conn = get_db_connection()
    conn.execute("DELETE FROM tasks WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect("/")


@app.route("/complete/<int:id>", methods=["POST"])
def complete(id):
    """Mark a task as completed."""
    conn = get_db_connection()
    conn.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for("home"))


@app.route("/", methods=["GET", "POST"])
def home():
    """Main route: handles displaying tasks and adding new tasks."""
    if request.method == "POST":
        # Get task content and list name from the form
        task_content = request.form.get("content")
        list_name = request.form.get("list_name", "General")

        # Only add non-empty tasks
        if task_content and task_content.strip():
            conn = get_db_connection()
            conn.execute(
                "INSERT INTO tasks (content, list_name) VALUES (?, ?)",
                (task_content.strip(), list_name),
            )
            conn.commit()
            conn.close()

        # Redirect to avoid form resubmission
        return redirect(url_for("home"))

    # Fetch all tasks from the database for display
    conn = get_db_connection()
    tasks = conn.execute("SELECT * FROM tasks").fetchall()
    conn.close()

    # Render the template with the list of tasks
    return render_template("index.html", tasks=tasks)


if __name__ == "__main__":
    # Run the Flask development server
    app.run(debug=True)