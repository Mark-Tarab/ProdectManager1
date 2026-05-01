from flask import Blueprint, render_template, request, redirect, session
from db import get_db

notes_bp = Blueprint("notes", __name__)

@notes_bp.route("/")
def home():
    return redirect("/notes")

@notes_bp.route("/notes", methods=["GET", "POST"])
def notes():
    if "user_id" not in session:
        return redirect("/login")

    db = get_db()
    cur = db.cursor()

    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        color = request.form["color"]

        cur.execute("INSERT INTO notes(title, content, color, is_pinned, user_id) VALUES(?,?,?,?,?)",
                    (title, content, color, 0, session["user_id"]))
        db.commit()

    cur.execute("SELECT * FROM notes WHERE user_id=? ORDER BY is_pinned DESC", (session["user_id"],))
    notes = cur.fetchall()

    return render_template("notes.html", notes=notes)

@notes_bp.route("/delete/<int:id>")
def delete(id):
    db = get_db()
    cur = db.cursor()
    cur.execute("DELETE FROM notes WHERE id=?", (id,))
    db.commit()
    return redirect("/notes")

@notes_bp.route("/pin/<int:id>")
def pin(id):
    db = get_db()
    cur = db.cursor()
    cur.execute("UPDATE notes SET is_pinned = 1 - is_pinned WHERE id=?", (id,))
    db.commit()
    return redirect("/notes")

@notes_bp.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    db = get_db()
    cur = db.cursor()

    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        color = request.form["color"]

        cur.execute("UPDATE notes SET title=?, content=?, color=? WHERE id=?",
                    (title, content, color, id))
        db.commit()
        return redirect("/notes")

    cur.execute("SELECT * FROM notes WHERE id=?", (id,))
    note = cur.fetchone()

    return render_template("edit.html", note=note)