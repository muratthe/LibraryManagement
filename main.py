class Library:
    def __init__(self, filename='books.txt'):
        self.file = open(filename, 'a+')
        self.filename = filename

    def __del__(self):
        self.file.close()

    def list_books(self):

        self.file.seek(0)
        lines = self.file.read().splitlines()
        for line in lines:
            book_info = line.split(',')
            print(f"Book: {book_info[0]},"
                  f" Author: {book_info[1]}")

    def add_book(self):
        # Add a book
        title = input("Enter the book title: ")
        author = input("Enter the book author: ")
        release_year = input("Enter the first release year: ")
        pages = input("Enter the number of pages: ")
        self.file.write(f"{title},{author},{release_year},{pages}\n")
        self.file.flush()

    def remove_book(self):
        title_to_remove = input("Enter the book title to remove: ")
        self.file.seek(0)
        lines = self.file.read().splitlines()
        self.file.close()
        with open(self.filename, 'w') as f:
            for line in lines:
                if not line.startswith(title_to_remove):
                    f.write(line + "\n")

    def menu(self):
        while True:
            print("--- MENU ---")
            print("1) List Books")
            print("2) Add Book")
            print("3) Remove Book")
            print("4) Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.list_books()
            elif choice == '2':
                self.add_book()
            elif choice == '3':
                self.remove_book()
            elif choice == '4':
                print("Exit the program.")
                break
            else:
                print("Invalid choice.")

lib = Library()

lib.menu()