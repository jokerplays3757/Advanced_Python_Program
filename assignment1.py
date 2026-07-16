#Assignment 1 : Write a program to create a simplified Library Management System using  object-oriented programming 
#principles in Python. This system should  manage books and patrons (library users), allowing for basic operations  
#such as adding new books, registering patrons, borrowing books, and  returning books.


class Book:
    def __init__(self, name, book_id, author):
        self.name = name
        self.book_id = book_id
        self.author = author
        self.IsBookBorrowed = False

class Patron:
    def __init__(self, name, patron_id):
        self.patron_id = patron_id
        self.name = name
        self.booksBorrowed = []

class Library:
    def __init__(self):
        self.listOfBooks = []
        self.listOfPatrons =[]
    def addBook(self, name, book_id, author):
        b = Book(name, book_id, author)
        self.listOfBooks.append(book_id)

    def registerPatron(self, name, patron_id):
        p = Patron(name, patron_id)
        self.listOfPatrons.append(patron_id)

    def Borrow(self, book, patron):
        if book.book_id not in self.listOfBooks:
            print("BOOK NOT AVAILABLE!\n")
            return
        

        
    
lib = Library()
print("WELCOME TO LIBRARY MANAGEMENT SYSTEM\n")
while True:
    x = int(input("1. Add Book\n2. Register Patron\n3. Borrow Book\n4. Return Book\n5. Exit\n"))
    if x == 1 :
        name = str(input("Enter the name of the book : \n"))
        book_id = int(input("Enter the id for the book : \n"))
        author = str(input("Enter the name of author for the book : \n"))
        lib.addBook(name, book_id, author)
    
    elif x == 2 :
        name = str(input("Enter the name of the Patron\n"))
        id = int(input("Enter the Patron Id no.\n"))
        lib.registerPatron(name, id)
    
    elif x == 3 :










