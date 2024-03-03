from collections import UserDict
import pickle

class AddressBook(UserDict):
    def __init__(self):
        super().__init__()

def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book.data, f)

def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            data = pickle.load(f)
            book = AddressBook()
            book.data.update(data)
            return book
    except FileNotFoundError:
        return AddressBook()

def main():
    book = load_data()
    save_data(book)

if __name__ == "__main__":
    main()
