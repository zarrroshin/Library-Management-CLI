import json 
from model.Book import Book
class StorageManager:
    @staticmethod
    def save_book(book:Book,filepath ='data/books.json' ):
        try : 
            with open(filepath,'r') as f : 
                data = json.load(f)
        except(FileNotFoundError,json.JSONDecodeError):
            data = []
        
        data.append(book.__dict__)

        with open(filepath,'w') as f : 
            json.dump(data,f,indent=2)