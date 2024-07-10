import copy
class Book:
    
    def __init__(self, title, author):
        
        self.title = title
        self.author = author
        self._is_checked_out = False
        
    def __str__(self):
        return f"{self.title} by {self.author}"  
        
    def check_out(self):
        self._is_checked_out = False
        
    def return_book(self):
        self._is_checked_out = True
        
  
    
class Library():
    
    
    def __init__(self):
        self._books = []
        self.copy_book = []
    
    def add_book(self, book):
        self._books.append(book)
        self.copy_book = copy.deepcopy(self._books)
    
    def check_out_book(self, title):
        for book in self._books:
            if title in str(book):
                self._books.remove(book)
                #self._book[2] = True
        
    def return_book(self, title):
        for copy_book in self.copy_book:
            for book in self._books:
                if copy_book != book and title in str(copy_book):
                    self._books.append(copy_book)
              
    def list_available_books(self):
        for book in self._books:
            print(book)
