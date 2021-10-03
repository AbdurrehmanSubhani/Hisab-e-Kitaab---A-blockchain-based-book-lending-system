from lms.book import Book


class Borrow:
    def __init__(self, book: Book, user: str):
        self.book = book
        self.user = user

    def __str__(self):
        return "user {0} is taking the book with details {1} ".format(self.user, str(self.book))
