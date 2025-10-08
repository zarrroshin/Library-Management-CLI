import json
class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author 
        self.is_borrowed = False
        self.member_id = None
        self.id = self.get_next_id()

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
                last_id = data.get("last_member_id", 1000)
        except json.JSONDecodeError:
            last_id = 1000
        

        # افزایش ID
        new_id = last_id + 1
        data["last_member_id"] = new_id

        # به‌روزرسانی فایل
        with open(tracker_path, "w") as f:
            json.dump(data, f, indent=2)

        return new_id

    