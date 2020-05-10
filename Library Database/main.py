class Book:
    title = "koi bhi title"
    author = "bandaro ka badsha"
    iSBN = 1234567891012

    def __init__(self,title,author,iSBN):
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
    db = []

    def insertBook(self,book):
        self.db.append(book)