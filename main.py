from blockchain.chain import Chain
from lms.book import Book
from lms.borrow import Borrow

chain = Chain(difficulty=20)


def enter_new_entry():
    isbn = input("Enter book isbn: ")
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    user = input("Who's taking the book? ")
    book = Book(isbn=isbn, title=title, author=author)
    borrow = Borrow(book=book, user=user)
    chain.add_data_to_pool(data=str(borrow))
    print("Started Mining...")
    chain.mine()
    print("Entry Added!")


def visualize_blockchain():
    print("Visualizing blockchain")
    chain.visualize_blockchain()


def main():
    while True:
        print("\n\n================================")
        print("Welcome to Fast Blockchain powered library management system")
        print("1: Enter a new entry")
        print("2: Visualize Blockchain")
        print("Q: Exit")
        option = input("Select an option: ")
        if option == "1":
            enter_new_entry()
        elif option == "2":
            visualize_blockchain()
        elif option == "Q" or option == "q":
            exit(0)
        else:
            print("Select a valid option!!")


if __name__ == "__main__":
    main()
