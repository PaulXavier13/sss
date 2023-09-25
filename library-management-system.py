import time

class Library:
    def __init__(self):
        # Initialize an empty list to store books
        self.books = []

    def add_book(self, title, author, pubYear):
        # Create a new Book object and add it to the library
        new_book = Book(title, author, pubYear)
        self.books.append(new_book)
        print(f"Book {title} added!")

    def remove_book(self, title):
        # Remove a book from the library by title
        for book in self.books[:]:
            if book.title == title:
                self.books.remove(book)
                print(f"Book {title} removed!")
                return
        print("Book not found!")

    def list_all_books(self):
        # List all books in the library
        for book in self.books:
            print(book)

    def search_book(self, title):
        # Search for a book by title and display its details
        for book in self.books:
            if book.title == title:
                print(book)
                return
        print("Book not found!")

    def update_book(self, title, new_title, new_author, new_pubYear):
        # Update book details (title, author, publication year)
        for book in self.books:
            if book.title == title:
                book.title = new_title if new_title else book.title
                book.author = new_author if new_author else book.author
                book.pubYear = new_pubYear if new_pubYear else book.pubYear
                print(f"Book {title} updated!")
                return
        print("Book not found!")

class Book:
    def __init__(self, title, author, pubYear):
        # Initialize book attributes: title, author, and publication year
        self.title = title
        self.author = author
        self.pubYear = pubYear

    def __str__(self):
        # Define a string representation for Book objects
        return f"{self.title} by {self.author} (Published in {self.pubYear})"

def main():
    # Create a Library instance
    library = Library()
    while True:
        print("\nLibrary Menu:")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List All Books")
        print("4. Search Book")
        print("5. Update Book")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter the book title: ")
            author = input("Enter the author's name: ")
            pubYear = input("Enter the publication year: ")
            library.add_book(title, author, pubYear)
        elif choice == "2":
            title = input("Enter the title of the book to remove: ")
            library.remove_book(title)
        elif choice == "3":
            library.list_all_books()
        elif choice == "4":
            title = input("Enter the title of the book to search: ")
            library.search_book(title)
        elif choice == "5":
            title = input("Enter the title of the book to update: ")
            new_title = input("Enter the new title: ")
            new_author = input("Enter the new author's name: ")
            new_pubYear = input("Enter the new publication year: ")
            library.update_book(title, new_title, new_author, new_pubYear)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

