class Person:
    checked_out_books = {}
    def __init__(self, first_name, last_name):
        self.fn = first_name
        self.ln = last_name
    def get_first_name(self):
        return self.fn
    def get_last_name(self):
        return self.ln

class Book:
    checked_out = False
    def __init__(self, title, author, id):
        self.t = title
        self.a = author
        self.id = id
    def get_title(self):
        return self.t
    def get_author(self):
        return self.a
    def get_id(self):
        return self.id
    def is_checked_out(self):
        return self.is_checked_out

class Library:
    def __init__(self, books):
        self.list_of_books = books
    def get_book(self):
        return self.bk
    def get_borrower(self):
        return self.brw
    def checkout(self, book, borrower):
        book.checked_out.__class__ = True
        self.list_of_books.pop(book.get_id())
        borrower.checked_out_books[book.get_id] = book
    def checkin(self, book, borrower):
        book.checked_out = False
        self.list_of_books[book.get_id()] = book
        borrower.checked_out_books.pop(book.get_id())