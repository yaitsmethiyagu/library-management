from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# import sqlite3
#
# db = sqlite3.connect("book_database.db")
# cursor = db.cursor()
# #
# # cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
#
#
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()
#

db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
db.init_app(app)


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book = db.Column(db.String(200), unique=True, nullable=False)
    author = db.Column(db.String(200), nullable=False)
    rating = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return "<Books %r>" % self.book


with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return "hello"

if __name__ == "__main__":

    app.run(debug=True)
