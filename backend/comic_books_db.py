from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from model import Base, Comentario

class Comic_Book(Base):
    __tablename__ = "comic_book"

    id = Column("pk_comic_book", Integer, primary_key=True)
    name = Column(String(120), unique=True)
    valor = Column(Float)
    state = Column(String(15))
    data_insercao = Column(DateTime, default=datetime.now())

    def doc_to_dict(doc):
        if not doc.exists:
            return None
        doc_dict = doc.to_dict()
        doc_dict['id'] = doc.id
        return doc_dict

    def read(book_id):
        """
        Return the details for a single comic book.
        """

        # retrieve a book from the database by ID
        book_ref = db.collection("books").document(book_id)
        return doc_to_dict(book_ref.get())


    def create(data):
        """
        Create a new comic book and return the comic book details.
        """

        book_ref = db.collection("books").document()
        book_ref.set(data)
        return doc_to_dict(book_ref.get())


    def update(data, book_id):
        """
        Update an existing comic book, and return the updated comic book's details.
        """

        book_ref = db.collection("books").document(book_id)
        book_ref.set(data)
        return doc_to_dict(book_ref.get())


    def delete(book_id):
        """
        Delete a comic book from the database.
        """

        book_ref = db.collection("books").document(book_id)
        book_ref.delete()
        # no return required


    def list():
        """
        Return a list of all comic books registered in the database.
        """
        # empty list of books
        comic_books = []

        docs = db.collection("books").order_by("title").stream()

        # retrieve each item in database and add to the list
        for doc in docs:
            books.append(doc_to_dict(doc))

        # return the list
        return books
