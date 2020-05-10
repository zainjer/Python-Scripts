import csv

# --------------- Design Structure -----------------

class Book:
    # --- Fields ---
    title = "Book Title"
    author = "Author Name"
    iSBN = 9783161484100

    # --- Methods ---
    def __init__(self, title, author, iSBN):
        self.title = title
        self.author = author
        self.iSBN = iSBN

    def getTitle(self):
        return self.title

    def getAuthor(self):
        return self.author

    def getISBN(self):
        return self.iSBN


class Database:
    # The list where 'Book' class objects are stored
    bookList = []

    # This method reads data from a csv and stores it on bookList
    def loadFromFile(self, filename):
        # Reads book data from any given file and stores it in 'rawList' variable
        rawList = []
        with open(filename, 'r', encoding="utf-8") as csv_file:
            rawList.__iadd__(csv.reader(csv_file))

        # Creates 'Book' objects from given data and stores each object in 'bookList'
        for row in rawList:
            book = Book(row[0], row[1], row[2])
            self.bookList.append(book)

    # This method writes all the data in 'bookList' on a csv file
    def saveToFile(self,filename):
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            for book in self.bookList:
                writer.writerow([book.getTitle(), book.getAuthor(), book.getISBN()])

    # This method takes a Book object as argument and inserts it into bookList
    def insertBook(self,newbook):
        self.bookList.append(newbook)

    # Takes in a string argument as 'author', and returns a list of 'Book' class objects that match
    def searchByAuthor(self,author):
        tempList = []
        for book in self.bookList:
            if book.getAuthor().find(author) > -1:
                tempList.append(book)
        return tempList


    # Takes in a string argument as 'title', and returns a list of 'Book' class objects that match
    def searchByTitle(self, title):
        tempList = []
        for book in self.bookList:
            if book.getTitle().find(title) > -1:
                tempList.append(book)
        return tempList

    # Takes in a string argument as 'ISBN', and returns the Book object that matches
    def searchByISBN(self, iSBN):
        tempList = []
        for book in self.bookList:
            if book.getISBN().find(iSBN) > -1:
                tempList.append(book)
        return tempList


# User Interaction Methods
def MainMenu():
    print("\n\n---------Main Menu------------")
    print("1. Add Book\n2. Search\n3. Exit")


    # User input selection conditions
    myinput = int(input())
    if myinput == 1:
        addBook()
    elif myinput == 2:
        SearchMenu()
    elif myinput == 3:
        myDatabase.saveToFile("data.csv")
        print('Thank you for using my application!')
        exit(1)
    else:
        print('Invalid Input! - Press Enter to Continue. ')
        # Blank Line enter
        input()

    MainMenu()

def addBook():
    print("\n----------ADD BOOK------------")
    print("Please enter book title: ")
    bookTitle = input()
    print("Please enter book author: ")
    bookAuthor = input()
    print("Please enter book ISBN: ")
    bookIBAN = int(input())

    newBook = Book(bookTitle, bookAuthor, bookIBAN)

    myDatabase.insertBook(newBook)
    print("\nBook Inserted!")
    MainMenu()


# Based on conditions, this method calls the searchBy_ methods in Database class, where each method returns a list of
# book objects that are stored in a separate list and printed out.
def SearchMenu():
    print("\n---------Search Menu------------")
    print("1. Title\n2. Author\n3. ISBN")
    myinput = int(input())
    result = []     # Stores the result list
    if myinput == 1:
        print("Enter Title: ")
        result = myDatabase.searchByTitle(input())
    elif myinput == 2:
        print("Enter Author: ")
        result = myDatabase.searchByAuthor(input())
    elif myinput == 3:
        print("Enter ISBN: ")
        result = myDatabase.searchByISBN(int(input()))
    else:
        print("Invalid Input! - Press Enter to Continue")
        input()                                 # Blank line enter
        SearchMenu()

    # Checks if the 'result' list contains any values, if it does Printing Values, otherwise show Not Found message
    if len(result)>0:
        for value in result:
            print("Title: "+value.getTitle()+"\t\tAuthor: "+value.getAuthor()+"\t\tISBN: "+str(value.getISBN()))
    else:
        print("No Books found as per given input")

    print("\n- Press Enter to go back to Main Menu")
    input()
    MainMenu()


# ------------------ Main Entry Point ---------------------
myDatabase = Database()                             # Creating Database object
myDatabase.loadFromFile("data.csv")                 # Load Books from given file
MainMenu()                                          # Starts Main Menu

