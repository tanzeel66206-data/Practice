class libraryItem:
    def __init__(self):
        pass

    def get_info(self):
        print("This is a library item.")

    def calculate_fine(self, days_overdue):
        fine = days_overdue * 0.5
        print(f"Fine for {days_overdue} days overdue: ${fine:.2f}")
    
class Book(libraryItem):

    def __init__(self,__title,__author,_genre):
        self.__title = __title
        self.__author = __author
        self._genre = _genre
        self.__pages = 300
        self.max_borrow_days = 14

    @property
    def pages(self):
        return self.__pages
    
    @pages.setter
    def pages(self, value):
        if value < 0:
            raise ValueError("Pages cannot be negative.")
        self.__pages = value

    def get_info(self):
        print(f"Title: {self.__title}")
        print(f"Author: {self.__author}")
        print(f"Genre: {self._genre}")

    def calculate_fine(self, days_overdue): # 10 rupees per day
        fine = days_overdue * 10
        print(f"Fine for {days_overdue} days overdue: Rs{fine:.2f}")

class Member:

    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books=[]

        
    def borrow_book(self,book):
        if len(self.borrowed_books) < 5:
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed {book._Book__title}.")
        else:
            print(f"{self.name} cannot borrow more than 5 books.")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            print(f"{self.name} returned {book._Book__title}.")
        else:
            print(f"{self.name} did not borrow {book._Book__title}.")

    def display_borrowed_books(self):
        if self.borrowed_books:
            print(f"{self.name} has borrowed the following books:")
            for book in self.borrowed_books:
                print(f"- {book._Book__title} by {book._Book__author}")

    

def search_books(books_list, title):
    if not books_list:
        return None
    return books_list[0] if books_list[0]._Book__title == title else search_books(books_list[1:], title)

def most_borrowed_book(borrow_dict):
    for book, count in borrow_dict.items():
        if count == max(borrow_dict.values()):
            return book

# Example usage

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Fiction")
book1.pages = 300
book2 = Book("To Kill a Mockingbird", "Harper Lee", "Fiction")
book2.pages = 350
book3 = Book("1984", "George Orwell", "Dystopian") 
book3.pages = 400
member1 = Member("Alice", "M001")
member2 = Member("Bob", "M002")
member1.borrow_book(book1)
member1.borrow_book(book2) 
member2.borrow_book(book3)
member1.display_borrowed_books()
member1.return_book(book1)
member1.display_borrowed_books()
books_list = [book1, book2, book3]
found_book = search_books(books_list, "1984")

if found_book:
    print(f"Book found: {found_book._Book__title} by {found_book._Book__author}")

borrow_dict = {book1: 5, book2: 3, book3: 7}
most_borrowed = most_borrowed_book(borrow_dict)
if most_borrowed:
    print(f"Most borrowed book: {most_borrowed._Book__title} by {most_borrowed._Book__author}")




