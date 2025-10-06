import json
class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author 
        self.is_borrowed = False
        self.member_id = None

    def borrow(self,member_id):
        if(self.is_borrowed):
            raise Exception("{} is not available".format(self.title))
        self.is_borrowed = True
        self.member_id = member_id

    def return_book(self,member_id):
        if(self.member_id != member_id):
            raise Exception("{} was not borrowed by this person".format(self.title))
        
        self.is_borrowed = False
        self.member_id = None

    def save_json(self):
        try : 
            with open('data/books.json','r') as f : 
                data = json.load(f)
        except(FileNotFoundError,json.JSONDecodeError):
            data = []
        
        data.append(self.__dict__)

        with open('data/books.json','w') as f : 
            json.dump(data,f,indent=2)
    

    
