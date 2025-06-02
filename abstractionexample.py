from abc import ABC, abstractmethod
class Item(ABC):
    def __init__(self, title):
        self.title = title
        self.is_borrowed = False

    @abstractmethod
    def borrow(self):
        pass

    @abstractmethod
    def return_item(self):
        pass
# Book class inherits from Item
class Book(Item):
    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"'{self.title}' has been borrowed.")
        else:
            print(f"'{self.title}' is already borrowed.")

    def return_item(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"'{self.title}' has been returned.")
        else:
            print(f"'{self.title}' was not borrowed.")

# Magazine class inherits from Item
class Magazine(Item):
    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"Magazine '{self.title}' has been borrowed.")
        else:
            print(f"Magazine '{self.title}' is already borrowed.")

    def return_item(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"Magazine '{self.title}' has been returned.")
        else:
            print(f"Magazine '{self.title}' was not borrowed.")

# DVD class inherits from Item
class DVD(Item):
    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"DVD '{self.title}' has been borrowed.")
        else:
            print(f"DVD '{self.title}' is already borrowed.")

    def return_item(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"DVD '{self.title}' has been returned.")
        else:
            print(f"DVD '{self.title}' was not borrowed.")


# Creating instances of each item type
book = Book("The Great Gatsby")
magazine = Magazine("National Geographic - July 2023")
dvd = DVD("Inception")

# Borrowing each item
book.borrow()        # Output: 'The Great Gatsby' has been borrowed.
magazine.borrow()    # Output: Magazine 'National Geographic - July 2023' has been borrowed.
dvd.borrow()         # Output: DVD 'Inception' has been borrowed.

# Attempting to borrow an item that's already borrowed
book.borrow()        # Output: 'The Great Gatsby' is already borrowed.

# Returning each item
book.return_item()   # Output: 'The Great Gatsby' has been returned.
magazine.return_item() # Output: Magazine 'National Geographic - July 2023' has been returned.
dvd.return_item()    # Output: DVD 'Inception' has been returned.


