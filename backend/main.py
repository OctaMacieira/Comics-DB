from flask import current_app, Flask, redirect, render_template
from flask import request, url_for
import logging

import comic_books_db

app = Flask(__name__)


@app.route('/')
def home():

    # get list of comic books
    comic_books = comic_books_db.list()

    # render homepage with list of comic books
    return render_template('index.html', comic_books=comic_books)


@app.route('/comic_books/<comic_book_id>')
def view(comic_book_id):
    # retrieve a specific book
    comic_book = comic_books_db.read(comic_book_id)

    # render book details
    return render_template('view.html', comic_book=comic_book)


@app.route('/comic-books/add', methods=['GET', 'POST'])
def add():
    """
    If GET, show the form to collect details of a new book.
    If POST, create the new book based on the specified form.
    """

    # Save details if form was posted
    if request.method == 'POST':

        # get book details from form
        data = request.form.to_dict(flat=True)

        # add book
        book = comic_books_db.create(data)

        # render book details
        return redirect(url_for('.view', book_id=book['id']))

    # render form to add book
    return render_template('form.html', action='Add', book={})


@app.route('/comic_books/<comic_book_id>/delete')
def delete(comic_book_id):
    """
    Delete the specified book and return to the book list.
    """

    # delete book
    comic_books_db.delete(comic_book_id)

    # render list of remaining books
    return redirect(url_for('.list'))


# this is only used when running locally
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)