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

    def showBooksBorrowed(self):
        print("List of books borrowed by", self.name, " : ")
        print("\nBook Name         Book ID\n")
        for b in self.booksBorrowed:
            print(b.name, "     ", b.book_id)
        

class Library:
    def __init__(self):
        self.listOfBooks = []
        self.listOfPatrons =[]
        self.available = []
    def addBook(self, name, book_id, author):
        b = Book(name, book_id, author)
        self.listOfBooks.append(b)
        self.available.append(book_id)

    def registerPatron(self, name, patron_id):
        p = Patron(name, patron_id)
        self.listOfPatrons.append(p)

    def Borrow(self, book_id, patron_id):
        patron_exists = False
        for p in self.listOfPatrons:
            if p.patron_id == patron_id:
                patron_exists = True
                if book_id not in self.available:
                    print("BOOK NOT AVAILABLE!\n")
                    return
                p.booksBorrowed.append(book_id)
                self.available.remove(book_id)
        
        if patron_exists == False:
            print("PATRON_ID IS INVALID")
            return
    
    def Return(self, book_id, patron_id):
        patron_exists = False
        for p in self.listOfPatrons:
            if p.patron_id == patron_id:
                patron_exists = True
                if book_id not in p.booksBorrowed:
                    print("NO RECORD OF BOOK BEING BORROWED\n")
                    return
                p.booksBorrowed.remove(book_id)
                self.available.append(book_id)
        if patron_exists == False:
            print("PATRON_ID IS INVALID")
            return

    def showBooks(self):
        print("Available Books :\nBOOK NAME      AUTHOR NAME     BOOK_ID\n")
        for i in self.available:
            for j in self.listOfBooks:
                if j.book_id == i:
                    print(j.name, "     ", j.author, "      ", j.book_id, "\n")

    def showPatrons(self):
        print("Registered Patrons :\nNAME     PATRON_ID")
        for i in self.listofPatrons:
            print(i.name, "     ", i.patron_id)

                   
    
lib = Library()
print("WELCOME TO LIBRARY MANAGEMENT SYSTEM\n")
while True:
    x = int(input("1. Add Book\n2. Register Patron\n3. Borrow Book\n4. Return Book\n5. Exit\n"))
    if x == 1 :
        name = str(input("Enter the name of the book : \n"))
        book_id = int(input("Enter the id for the book : \n"))
        author = str(input("Enter the name of author for the book : \n"))
        lib.addBook(name, book_id, author)
        lib.showBooks()
    
    elif x == 2 :
        name = str(input("Enter the name of the Patron\n"))
        id = int(input("Enter the Patron Id no.\n"))
        lib.registerPatron(name, id)
        lib.showPatrons()
    
    elif x == 3 :
        p = Patron()
        id = int(input("Enter the ID of the book you want to borrow : \n"))
        p_id = int(input("Enter the patron ID no. : "))
        for i in lib.listOfPatrons:
            if i.patron_id == p_id:
                lib.Borrow(id, i)
                break
        lib.showBooks()
        p.showBooksBorrowed()

    
    elif x == 4:
        p = Patron()
        id = int(input("Enter the ID of the book you want to return : \n"))
        p_id = int(input("Enter the patron ID no. : "))
        for i in lib.listOfPatrons:
            if i.patron_id == p_id:
                lib.Return(id, i)
                break
        lib.showBooks()
        p.showBooksBorrowed()
    elif x == 5:
        print("\nGOODBYE\n")
        break











