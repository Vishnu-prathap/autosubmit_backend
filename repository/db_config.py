from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

DB_NAME = "quiz__app"
DB_USER = "postgres"
DB_PASSWORD = "your_password"
DB_HOST = "localhost"
DB_PORT = "5433"


app.config['SQLALCHEMY_DATABASE_URI'] =f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
app.config[''] = False

db = SQLAlchemy(app)
with app.app_context():
    db.create_all()
    print("Database connected and tables created.")
