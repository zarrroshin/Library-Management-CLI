from view.menu_view import MenuView
from model.Book import Book
from model.Member import Member
from model.StorageManager import StorageManager

class LibraryController:
   
   
   def __init__(self):
      self.MenuView = MenuView()
      self.Storage = StorageManager()
   
   
   
   def add_book(self):
      data = self.MenuView.add_book()
      book = Book(data['title'],data['author'])
      self.Storage.save(book)

      
      
   
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
      data = self.MenuView.add_member()
      member = Member(data["name"],data["email"])
      self.Storage.save(member,'data/members.json')

   
   def show_books(self):
      data = self.Storage.load_books()
      self.MenuView.show_books(data)
   
   def borrow_book(self):
      title = self.MenuView.ask_for_title()
      
   
   def return_book(self):
      pass