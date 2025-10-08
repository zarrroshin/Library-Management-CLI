from controller.library_controller import LibraryController

def main():
    controller = LibraryController()
    while True: 
    # implementing a simple CLI 
        print("""choose one: 
            1)Add book
            2)Remove book
            3)Search book
            4)adding a member
            5)showing list of books
            6)borrow book
            7)return book
            8)save and exit """)

        command = input("enter a number : ")

        try: 
            if command == "1":
                controller.add_book()
            
            elif command =="2":
                controller.remove_book()
            
            elif command=="3":
                controller.search_book()

            elif command == "4":
                controller.add_member()
            
            elif command=="5":
                controller.show_books()

            elif command =="6":
                controller.borrow_book()

            elif command == "7":
                controller.return_book()

            elif command=="8":
                print("Goodbye!")
                break                
            
            else:
                print("Invalid choice, please try again")
            

        except Exception as e : 
            print(f"erorr: {e}")

if __name__=="__main__":
    main()

