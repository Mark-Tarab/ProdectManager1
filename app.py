from flask import Flask
from db import init_db
from auth import auth_bp
from notes import notes_bp

app = Flask(__name__)
app.secret_key = "secret"

init_db()

app.register_blueprint(auth_bp)
app.register_blueprint(notes_bp)

if __name__ == "__main__":
    app.run(debug=True)