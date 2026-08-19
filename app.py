from flask import Flask, Blueprint, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__, static_url_path="/saurav/static")
bp = Blueprint("task_manager", __name__, url_prefix="/saurav")
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tasks.db")


def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db_connection()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            completed INTEGER NOT NULL DEFAULT 0
        )
        """
    )
    conn.commit()
    conn.close()


@bp.route("/")
def index():
    conn = get_db_connection()
    tasks = conn.execute("SELECT * FROM tasks ORDER BY id DESC").fetchall()
    conn.close()
    return render_template("index.html", tasks=tasks)


@bp.route("/add", methods=["POST"])
def add_task():
    title = request.form.get("title", "").strip()
    if title:
        conn = get_db_connection()
        conn.execute("INSERT INTO tasks (title, completed) VALUES (?, 0)", (title,))
        conn.commit()
        conn.close()
    return redirect(url_for("task_manager.index"))


@bp.route("/complete/<int:task_id>")
def complete_task(task_id):
    conn = get_db_connection()
    conn.execute("UPDATE tasks SET completed = 1 - completed WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    return redirect(url_for("task_manager.index"))


@bp.route("/delete/<int:task_id>")
def delete_task(task_id):
    conn = get_db_connection()
    conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    return redirect(url_for("task_manager.index"))


app.register_blueprint(bp)

init_db()

if __name__ == "__main__":
    app.run(debug=True)
