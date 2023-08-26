from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///virtual-library.db"

db.init_app(app)

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Books {self.title}>'

with app.app_context():
    db.create_all()

# all_books = []


@app.route('/')
def home():
    with app.app_context():
        all_books = db.session.execute(db.select(Books).order_by(Books.id)).scalars().all()
    return render_template('index.html', books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        
        # new_book = {
        #     "title": request.form["title"],
        #     "author": request.form["author"],
        #     "rating": request.form["rating"],
        # }
        # all_books.append(new_book)

        book_title = request.form["title"]
        book_author = request.form["author"]
        book_rating = request.form["rating"]
        
        # insert new data into the database
        with app.app_context():
            new_book = Books(title=book_title, author=book_author, rating=book_rating)
            db.session.add(new_book)
            db.session.commit()
        
        return redirect(url_for('home'))

    return render_template('add.html')

@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        book_id = request.form["book_id"]
        new_rating = request.form["new_rating"]
        book_to_update = db.get_or_404(Books, book_id)
        book_to_update.rating = new_rating
        db.session.commit()
        # with app.app_context():
        #     book_to_update = db.session.execute(db.select(Books).where(Books.id == book_id)).scalar()
        #     book_to_update.rating = new_rating
        #     db.session.commit()
        
        return redirect(url_for('home'))

    book_id = request.args.get('id')
    book_selected = db.get_or_404(Books, book_id)

    return render_template('edit_rating.html', book_to_update=book_selected)

@app.route("/delete")
def delete_book():
    book_id = request.args.get('id')
    book_to_remove = db.get_or_404(Books, book_id)
    db.session.delete(book_to_remove)
    db.session.commit()

    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)

