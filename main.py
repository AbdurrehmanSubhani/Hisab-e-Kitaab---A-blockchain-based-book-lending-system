from blockchain.chain import Chain
from blockchain.client import Client
from lms.book import Book
from lms.borrow import Borrow

chain = Chain(difficulty=20)


def enter_new_entry():
    isbn = input("Enter book isbn: ")
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    user = input("Who's taking the book? ")
    book = Book(isbn=isbn, title=title, author=author, booked=False)
    print("Checking book availability")
    borrow = Borrow(book=book, user=user)
    chain.add_data_to_pool(data=borrow)
    available = chain.check_book_availability(isbn, title, author)
    if available:
        print("Started Mining...")
        chain.mine(False)
        print("Entry Added!")
    else:
        print("Please choose a different book")


def visualize_blockchain():
    print("Visualizing blockchain")
    chain.visualize_blockchain()


def return_book():
    isbn = input("Enter book isbn: ")
    chain.return_book(isbn=isbn)


def main():
    while True:
        print("\n\n================================")
        print("Welcome to Fast Blockchain powered library management system")
        print("1: Enter a new entry")
        print("2: Visualize Blockchain")
        print("3: Return book")
        print("Q: Exit")
        option = input("Select an option: ")
        if option == "1":
            enter_new_entry()
        elif option == "2":
            visualize_blockchain()
        elif option == "3":
            return_book()
        elif option == "Q" or option == "q":
            exit(0)
        else:
            print("Select a valid option!!")


if __name__ == "__main__":
    main()
