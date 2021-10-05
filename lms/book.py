class Book:
    def __init__(self, isbn: str, title: str, author: str,booked):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.booked = booked

    def __str__(self):
        return "ISBN: {0} Book Title: {1} Author: {2} Booked: {3} \n".format(self.isbn, self.title, self.author,self.booked)
