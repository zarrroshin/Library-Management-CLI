
class MenuView:
    
    def add_book(self):
        title = input("Enter name of book: ")
        author = input("Enter author of book: ")
        return {"title":title,"author":author}
    
    def remove_book(self):
        title = input("which book do you want to delete? ")
        return title
    

    def show_error(self):
        print("this book doesn't exist in our library")