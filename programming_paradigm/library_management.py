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
        self._book = []
    
    def add_book(self, book):
        self._book.append(book)
    
    def check_out_book(self, title):
        for book in self._book:
            if title in str(book):
                self._book.remove(book)
                #self._book[2] = True
        
    def return_book(self, title):
        for book in self._book:
            if title in str(book):
                self._book.append(book)
                #self._book[2] = False
                
    def list_available_books(self):
        for book in self._book:
            print(book)
        

