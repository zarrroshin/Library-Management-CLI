import json
class Member:
    def __init__(self,name,email):
        self.name= name
        self.email = email
        self.borrowed_books = []
        self.id = self.get_next_id()
    
    def borrow_book(self,book):
        pass

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

        # به‌روزرسانی فایل
        with open(tracker_path, "w") as f:
            json.dump(data, f, indent=2)

        return new_id