from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///books_data.db'
db.init_app(app=app)


all_books = []


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book = db.Column(db.String(200), unique=True, nullable=False)
    author = db.Column(db.String(200), nullable=False)
    rating = db.Column(db.String(2), nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    data = db.session.query(Books).all()


    # return render_template("index.html", all_books=all_books)

    return render_template("index.html", all_books=data)



@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "GET":
        return render_template("add.html")
    else:
        # book_review = {
        #     "Book_name": request.form["book"],
        #     "Book_author": request.form["author"],
        #     "rating": request.form["rating"]
        # }
        # all_books.append(book_review)

        book_review = Books(book= request.form["book"],
                            author = request.form["author"],
                            rating = request.form["rating"]
                            )
        db.session.add(book_review)
        db.session.commit()


        return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
