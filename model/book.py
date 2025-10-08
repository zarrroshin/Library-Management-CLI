import json
class Book:
    def __init__(self,title,author):
        self.__title = title
        self.__author = author 
        self.__is_borrowed = False
        self.__member_id = None
        self.__id = self.get_next_id()
    
    @property
    def title(self):
        return self.__title
    
    @is_borrowed.setter
    def is_borrowed(self,value):
        self.__is_borrowed = value

        
    @property
    def is_borrowed(self):
        return self.__is_borrowed

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
    
    
    @staticmethod
    def get_next_id():
        tracker_path = "data/id_tracker.json"
        try:
            with open(tracker_path, "r") as f:
                data = json.load(f)
                last_id = data.get("last_book_id", 1000)
        except json.JSONDecodeError:
            last_id = 1000
        

        # افزایش ID
        new_id = last_id + 1
        data["last_book_id"] = new_id

     
        with open(tracker_path, "w") as f:
            json.dump(data, f, indent=2)

        return new_id

    