class Book:

    def __init__(self,title,author,price,language):
        self.title=title
        self.author=author
        self.price=price
        self.language=language

    def print_details(self):
        print(self.title,self.author,self.price,self.language)

book_instance=Book("looking for alaska","John Green",350,"english")
book_instance.print_details()
print(book_instance)