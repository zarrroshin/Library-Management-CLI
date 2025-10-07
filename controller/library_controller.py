from view.menu_view import MenuView
from model.Book import Book
from model.StorageManager import StorageManager

class LibraryController:
   
   
   def __init__(self):
      self.MenuView = MenuView()
      self.Storage = StorageManager()
   
   
   
   def add_book(self):
      data = self.MenuView.add_book()
      book = Book(data['title'],data['author'])
      self.Storage.save_book(book)

      
      
   
   def remove_book(self):
        data = self.MenuView.remove_book()
        try:
           self.Storage.remove_book(data)
        except:
           self.MenuView.remove_error()
   
   
   def search_book(self):
      data = self.MenuView.search_book()
      try:
         book = self.Storage.search_book(data)
         self.MenuView.show_book(book)
         
      except:
         self.MenuView.search_error(data)
   
   def add_member(self):
      pass
   
   def show_books(self):
      pass
   
   def borrow_book(self):
      pass
   
   def return_book(self):
      pass