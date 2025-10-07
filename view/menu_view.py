
class MenuView:
    
    def add_book(self):
        title = input("Enter name of book: ")
        author = input("Enter author of book: ")
        return {"title":title,"author":author}