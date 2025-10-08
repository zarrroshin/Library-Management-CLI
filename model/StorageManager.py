import json 
from model.Book import Book
from model.Member import Member
class StorageManager:

    def load_books(self,filepath ='data/books.json' ):
        try : 
            with open(filepath,'r') as f : 
                data = json.load(f)
        except(FileNotFoundError,json.JSONDecodeError):
            data = []
        return data

    def save(self,obj,filepath ='data/books.json' ):
        try : 
            with open(filepath,'r') as f : 
                data = json.load(f)
        except(FileNotFoundError,json.JSONDecodeError):
            data = []
        
        data.append(obj.__dict__)

        with open(filepath,'w') as f : 
            json.dump(data,f,indent=2)

        
    def remove_book(self,title,filepath ='data/books.json'):
        with open(filepath,'r') as f :
            data = json.load(f)
        deleted = False
        for obj in data: 
            if obj["title"] == title :
                data.remove(obj)
                deleted = True
        if(deleted):
            with open(filepath,'w') as f : 
                json.dump(data,f,indent=2)
        else : 
            raise Exception
        

    def search_book(self,title,filepath='data/books.json'):
        with open(filepath,'r') as f :
            data = json.load(f)
        for obj in data: 
            if obj["title"] == title :
                return obj
         
        raise Exception
    

    def search_member(self,id,filepath='data/members.json'):
        with open(filepath,'r') as f :
            data = json.load(f)
        for obj in data: 
            if obj["id"] == id :
                return obj
         
        raise Exception
    

    
    def update_book(self, book):
            data = self.load_books()

            for i, b in enumerate(data):
                if b['title'] == book["title"]:
                    data[i] = book
                    break
            
            with open("data/books.json","w") as f : 
                json.dump(data,f,indent=2)


    def update_member(self, member):
        data = self.load_books("data/members.json")

        for i, b in enumerate(data):
            if b['id'] == member["id"]:
                data[i] = member
                break
        
        with open("data/members.json","w") as f : 
            json.dump(data,f,indent=2)