# 📚 Library Management System

A simple and structured **Library Management System** built using **Python (OOP + MVC Architecture)**.  
This project allows you to manage books and members, track borrowed books, and save data in JSON files.

---

## 🚀 Features

- 📘 Add and remove books  
- 👩‍💻 Register and remove members  
- 🔄 Borrow and return books  
- 💾 Persistent data storage using JSON  
- 🧠 Object-Oriented Design with encapsulation and properties  
- 🧩 Organized using MVC (Model–View–Controller) architecture  

---

## 🏗️ Project Structure

Library-Management-System/
│
├── controller/
│ └── library_controller.py
│
├── model/
│ ├── book.py
│ ├── member.py
│ └── storage_manager.py
│
├── view/
│ └── menu_view.py
│
├── data/
│ ├── books.json
│ ├── members.json
│ └── id_tracker.json
│
├── main.py
└── README.md

yaml
Copy code

---

## ⚙️ How to Run

### 1️⃣ Clone the repository

```bash
git clone https://github.com/zarrroshin/Library-Management-System.git
cd Library-Management-System
2️⃣ Run the main program
```bash
Copy code
python main.py
3️⃣ Follow the menu
You can:

Add or remove books

Register or delete members

Borrow or return books

View all books and members

💡 Technical Details
Language: Python 3.10+

Architecture: MVC

Data Storage: JSON files

Concepts used:

Classes and Objects

Encapsulation

Class variables and instance variables

File handling and JSON serialization

🧠 Example JSON (data/id_tracker.json)
json
Copy code
{
  "last_book_id": 1002,
  "last_member_id": 1005
}
📈 Future Improvements
Add search functionality

Add GUI using Tkinter or Flask

Add date tracking for borrowed books

Support exporting reports in CSV or PDF

👩‍💻 Author
Zahra Roshani
📧 zahraroshani973@gmail.com
🌐 GitHub | LinkedIn