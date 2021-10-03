class Book:
    def __init__(self, isbn, title, author):
        self.isbn = isbn
        self.title = title
        self.author = author

    def __str__(self):
        return "ISBN: {0} Book Title: {1} Author: {2} \n".format(self.isbn, self.title, self.author)
