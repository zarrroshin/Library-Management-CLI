class MenuView:
    def add_book(self):
        title = input("Enter name of book: ")
        author = input("Enter author of book: ")
        return {"title":title,"author":author}
    
    def remove_book(self):
        title = input("which book do you want to delete? ")
        return title
    

    def remove_error(self):
        print("this book doesn't exist in our library")

    
    def search_book(self):
        title = input("Enter name of book : ")
        return title
    
    def search_error(self,title):
        print(f"{title} doesn't exist")

    def show_book(self,book):
        if(book["is_borrowed"]):
            print(f"title: {book["title"]},is_borrowed: {book["is_borrowed"]},author: {book["author"]},borrowed by: {book["member_id"]}")

        else:
            print(f"title: {book["title"]},is_borrowed: {book["is_borrowed"]},author: {book["author"]}")
        