from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# expenses = []

def get_db_connection():
    conn = sqlite3.connect("expenses.db")
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db_connection()

    conn.execute("""

            CREATE TABLE IF NOT EXISTS expenses(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            description TEXT
            )
""")
    conn.commit()
    conn.close()


@app.route("/")
def home():
    conn = get_db_connection()

    expenses = conn.execute(
        "SELECT * FROM expenses"
    ).fetchall()

    conn.close()

    total = 0

    for expense in expenses:
        total += float(expense["amount"])

    return render_template("index.html",expenses=expenses, total=total)


@app.route("/add", methods=["POST"])
def add_expense():

    amount = request.form["amount"]
    if not amount:
        return "Amount is required"

    try:
        amount = float(amount)
    except ValueError:
        return "Amount must be a number"
    if amount <= 0:
        return "Amount must be greater than 0"
    
    category = request.form["category"].strip()
    if not category:
        return "Category is required"
    
    description = request.form["description"]

    if not description:
        return "Description is required"

    conn = get_db_connection()

    conn.execute(
        "INSERT INTO expenses (amount, category, description) VALUES (?, ?, ?)",
        (amount, category, description)
    )

    conn.commit()
    conn.close()

    return redirect("/")


@app.route("/edit", methods=["POST"])
def edit_expense():
    expense_id = int(request.form["id"])

    conn = get_db_connection()

    expense = conn.execute(
        "SELECT * FROM expenses WHERE id = ?",
        (expense_id,)
    ).fetchone()

    conn.close()

    return render_template("edit.html", expense=expense)


@app.route("/update", methods=["POST"])
def update_expense():
    
    expense_id = int(request.form["id"])
    amount = request.form["amount"]

    if not amount:
        return "Amount is required"

    try:
            amount = float(amount)
    except ValueError:
        return "Amount must be a number"

    if amount <= 0:
        return "Amount must be greater than 0"

    category = request.form["category"].strip()

    if not category:
        return "Category is required"

    description = request.form["description"]

    conn = get_db_connection()

    conn.execute(
        """
        UPDATE expenses
        SET amount = ?, category = ?, description = ?
        WHERE id = ?
        """,
        (amount, category, description, expense_id)
    )

    conn.commit()
    conn.close()

    return redirect("/")


@app.route("/delete", methods=["POST"])
def delete_expense():
    expense_id =int( request.form["id"])

    conn = get_db_connection()

    conn.execute(
        "DELETE FROM expenses WHERE id = ?",
        (expense_id,)
    )

    conn.commit()
    conn.close()

    return redirect("/")

init_db()

if __name__ == "__main__":
    app.run(debug=True)