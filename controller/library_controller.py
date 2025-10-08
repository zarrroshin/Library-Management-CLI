from view.menu_view import MenuView
from model.book import Book
from model.member import Member
from model.storage_manager import StorageManager

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
      self.MenuView.show_id(member)
      self.Storage.save(member,'data/members.json')

   
   def show_books(self):
      data = self.Storage.load()
      self.MenuView.show_books(data)
   
   def borrow_book(self):
      data = self.MenuView.borrow_book()
      try:
         id =int(data["id"])
         member = self.Storage.search_member(id)
         try : 
            book = self.Storage.search_book(data["title"])
            if not book["is_borrowed"]:
               book["is_borrowed"] = True
               book["member_id"] = id
               self.Storage.update_book(book)
               member["borrowed_books"].append(data["title"])
               self.Storage.update_member(member)
            else:
               print("this book is already borrowed ")
         except: 
            print("this book doesn't exist")
      except:
         print("you are not a member please sign up")
      
   
   def return_book(self):
      data = self.MenuView.borrow_book()
      try:
         id =int(data["id"])
         member = self.Storage.search_member(id)
         try : 
            book = self.Storage.search_book(data["title"])
            if book["member_id"] == id : 
               book["member_id"] = None
               book["is_borrowed"] = False
               self.Storage.update_book(book)
               member["borrowed_books"].remove(data["title"])
               self.Storage.update_member(member)
            else:
               print("this book was not borrowed by this id")      
         except: 
            print("this book doesn't exist")
      except:
         print("you are not a member please sign up")
      