#Bài 2

class Student:

    def __init__(self, name, score):
        self.name = name
        self.__score = score

    def change_score(self, score):
        if score >= 0 and score <= 10:
            self.__score = score
            print(f"Thay đổi điểm của {self.name} thành công!")
        else:
            print("Điểm không hợp lệ!")
    
    def get_score(self):
        return self.__score

    def show_info(self):
        print(f'Tên: {self.name}\nĐiểm: {self.__score}')

s1 = Student("Tú", 8)
s1.change_score(9)
s1.change_score(100)
print(s1.get_score())
s1.show_info()

#Bài 3

class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
    
    def change_pages(self, book, pages):
        if book.set_pages(pages):
            print("Thay đổi số trang thành công!")
        else:
            print("Số trang không hợp lệ!")

class Book:

    def __init__(self, author, book, pages):
        self.author = author
        self.book = book
        self.__pages = pages

    def set_pages(self, pages):
        if pages >= 0:
            self.__pages = pages
            return True
        return False

    def __str__(self):
        return f'Tác giả: {self.author}\nTên sách: {self.book}\n{self.__pages} chương'

book = Book("Con", "CCN", 920)
my_lib = Library()
my_lib.add_book(book)
for book in my_lib.books:
    print(book)
my_lib.change_pages(book, 200)
for book in my_lib.books:
    print(book)