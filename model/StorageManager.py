import json 
from model.Book import Book
class StorageManager:
    def save_book(self,book:Book,filepath ='data/books.json' ):
        try : 
            with open(filepath,'r') as f : 
                data = json.load(f)
        except(FileNotFoundError,json.JSONDecodeError):
            data = []
        
        data.append(book.__dict__)

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
                found = True
                return obj
         
        raise Exception
        