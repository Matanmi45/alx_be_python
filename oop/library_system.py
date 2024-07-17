class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
    def __str__(self):
        return f"Book: {self.title} by {self.author}"
    


class EBook(Book):
    def __init__(self, title, author, file_size):
        self.file_size = file_size
        super().__init__(title, author)
        
    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"    


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        self.page_count = page_count
        super().__init__(title, author)
        
    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"    


class Library():
    def __init__(self):
        self.booklist = []
        
    def add_book(self, book):
        self.booklist.append(book)
        
    def list_books(self):
        for book in self.booklist:
            print(book)
        
def main():
    # Create a Library instance
    my_library = Library()

    # Create instances of each type of book
    classic_book = Book("Pride and Prejudice", "Jane Austen")
    digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
    paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    # Add books to the library
    my_library.add_book(classic_book)
    my_library.add_book(digital_novel)
    my_library.add_book(paper_novel)

    # List all books in the library
    my_library.list_books()

if __name__ == "__main__":
    main()
    
#main()    
        
        
        
        
        