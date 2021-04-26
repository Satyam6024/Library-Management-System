import datetime
import os
# os.getcwd()

class LMS:      # This class is used to keep records of the books in the Library
    def __init__(self, list_of_books, library_name):
        self.list_of_books = "List_of_books.txt"
        self.library_name = library_name
        self.books_dict = {}
        Id = 101
        with open(self.list_of_books) as bk:
            content = bk.readlines()
        for line in content:
            # print(line)
            self.books_dict.update({str(Id):{'Books_title':line.replace("\n",""), 'Lender_name':"", 'Issue_date':"", 'Status':"Available"}})
            Id = Id+1

    def display_books(self):        #Display Book ID and Title of the Books
        print("------------List of Books-----------")
        print("Book ID", "\t", "Title")
        print("------------------------------------")
        for key, value in self.books_dict.items():
            print(key, "\t\t", value.get("Books_title"), "- [", value.get("Status"), "]")


    def issue_books(self):      #Issues the book according to Book ID if available, if someone has already issued than it will show who and when the person has issued, and if someone give an unknown book is than it will show that this Book ID not found
        books_id = input("Enter book's ID: ")
        current_date = datetime.datetime.now().strftime("%d-%m-%Y   %H:%M:%S")

        if books_id in self.books_dict.keys():
            if not self.books_dict[books_id]["Status"] == "Available":
                print(f"This book is already issued to {self.books_dict[books_id]['Lender_name']} on {self.books_dict[books_id]['Issue_date']}")
                return self.issue_books()

            elif self.books_dict[books_id]["Status"] == "Available":
                your_name = input("Enter your name: ")
                self.books_dict[books_id]["Lender_name"] = your_name
                self.books_dict[books_id]["Issue_date"] = current_date
                self.books_dict[books_id]["Status"] = "Already Issued"
                print("Books Issued Successfully !!!\n")

            else:
                print("Book ID not found !!!")
                return self.issue_books()

    
    def add_books(self):        #To add New Books to the library
        new_books = input("Enter Book's Title: ")
        if new_books == "":
            return self.add_books()
        elif len(new_books)>30:
            print("Length of Book's Title is too long !!!   Title length must min 3 characters and max 25 characters...")
            return self.add_books
        else:
            with open(self.list_of_books, "a") as bk:
                bk.writelines(f"{new_books}\n")
                self.books_dict.update({str(int(max(self.books_dict))+1):{'Books_title':new_books, 'Lender_name':"", 'Issue_date':"", 'Status':"Available"}})
                print(f"This book '{new_books}' has been added successfully !!!")


    def return_books(self):     #To return a Book
        books_id = input("Enter books ID: ")
        if books_id in self.books_dict.keys():
            if self.books_dict[books_id]["Status"] == "Available":
                print("This book is already available in library. Please check your Book ID !!!")      
                return self.return_books()
            elif not self.books_dict[books_id]["Status"] == "Available":
                self.books_dict[books_id]["Lender_name"] = ""
                self.books_dict[books_id]["Issued_date"] = ""
                self.books_dict[books_id]["Status"] = "Available"
                print("Successfully Updated !!!\n")
            else:
                print("Book ID is not found")

try:
    myLMS = LMS("list_of_books.txt", "Satyam's")
    press_key_list = {"D":"Display Books", "I":"Issue Books", "A":"Add Books", "R":"Return Books", "Q":"Quit"}
    key_press = False
    while not (key_press == "q"):
        print(f"\n--------------- Welcome to {myLMS.library_name} Library Management System----------------\n")
        for key, value in press_key_list.items():
            print("Press", key, "To", value)
        key_press = input("Press key: ").lower()
        if key_press == "i":
            print("\nCurrent Selection : Issuing of Book\n")
            myLMS.issue_books()
        elif key_press == "a":
            print("\nCurrent Selection : Adding a Book\n")
            myLMS.add_books()
        elif key_press == "d":
            print("\nCurrent Selection : Displaying the Book\n")
            myLMS.display_books()
        elif key_press == "r":
            print("\nCurrent Selection : Returning the Book\n")
            myLMS.return_books()
        elif key_press == "q":
            break
        else:
            continue
except Exception as e:
    print("Something went wrong. Please check your input !!!")


# l = LMS("List_of_books.txt", "Python's Library")
# print(l.display_books())