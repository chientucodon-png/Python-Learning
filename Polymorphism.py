#bài 1

class Animal:

    def sound(self):
        print("Peter peter!")

class Dog(Animal):

    def sound(self):
        print("Woof woof!")

class Cat(Animal):
    
    def sound(self):
        print("Meow meow!")

class Bird(Animal):

    def sound(self):
        print("Chip chip!")

d1 = Dog()
c1 = Cat()
b1 = Bird()
animals = [d1, c1, b1]

for animal in animals:
    animal.sound()
#bài 2

class Vehical:

    def start_engine(self):
        print("Vehical start engine!")

class Car(Vehical):

    def start_engine(self):
        print("Car start engine!")

class Motorbike(Vehical):
    
    def start_engine(self):
        print("Motorbike start engine!")

class Bus(Vehical):

    def start_engine(self):
        print("Bus start engine!")

c1 = Car()
m1 = Motorbike()
b1 = Bus()

vehicals = [c1, m1, b1]

for vehical in vehicals:
    vehical.start_engine()

#bài 3

class Employee():
    
    def __init__(self, name):
        self.name = name

    def work(self):
        print(f'{self.name}: Work')

class Programmar(Employee):

    def work(self):
        print(f'{self.name}: Programmer')

class Designer(Employee):

    def work(self):
        print(f'{self.name}: Designer')

class Manager(Employee):

    def work(self):
        print(f'{self.name}: Manager')

p1 = Programmar("An")
d1 = Designer("Jimmy")
m1 = Manager("Cloe")

employees = [p1, d1, m1]

for employee in employees:
    employee.work()

#bài 4

class Book():

    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def show_info(self):
        print(f'Tên sách: {self.title}')
        print(f'Tác giả: {self.author}')

class Novel(Book):

    def __init__(self, title, author, genre):
        super().__init__(title, author)
        self.genre = genre

    def show_info(self):
        print(f'Tên sách: {self.title}')
        print(f'Tác giả: {self.author}')
        print(f'Thể loại: {self.genre}')

class Comic(Book):

    def __init__(self, title, author, illustrator):
        super().__init__(title, author)
        self.illustrator = illustrator

    def show_info(self):
        print(f'Tên sách: {self.title}')
        print(f'Tác giả: {self.author}')
        print(f'Họa sĩ: {self.illustrator}')

class TextBook(Book):

    def __init__(self, title, author, subject):
        super().__init__(title, author)
        self.subject = subject

    def show_info(self):
        print(f'Tên sách: {self.title}')
        print(f'Tác giả: {self.author}')
        print(f'Môn học: {self.subject}')

n1 = Novel("Cổ Chân Nhân", "Cổ Chân Nhân", "Huyền huyễn")
c1 = Comic("Chiêu Hồng Nguyệt", "Phạm Minh Khai", "Phạm Minh Khai")
t1 = TextBook("Sách vật lí 12", "NXB Long Châu", "Vật lí")
books = [n1, c1, t1]
stt = 1
for book in books:
    print(f"Cuốn {stt}")
    book.show_info()
    stt += 1

#bài 5

class Shape:

    def __init__(self, name):
        self.name = name

    def area(self):
        pass
    
class Rectangle(Shape):

    def __init__(self, name, chieu_dai, chieu_rong):
        super().__init__(name)
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong

    def area(self):
        dien_tich = self.chieu_dai * self.chieu_rong
        print(f'Diện tích {self.name} là: {dien_tich}')

class Circle(Shape):

    def __init__(self, name, ban_kinh):
        super().__init__(name)
        self.ban_kinh = ban_kinh

    def area(self):
        dien_tich = 3.14 * self.ban_kinh ** 2
        print(f'Diện tích {self.name} là: {dien_tich}')

class Triangle(Shape):

    def __init__(self, name, chieu_dai_day, chieu_cao):
        super().__init__(name)
        self.chieu_dai_day = chieu_dai_day
        self.chieu_cao = chieu_cao

    def area(self):
        dien_tich = self.chieu_dai_day * self.chieu_cao / 2
        print(f'Diện tích {self.name} là: {dien_tich}')

hinh_chu_nhat = Rectangle("Hình chữ nhật", 5, 3)
hinh_tron = Circle("Hình tròn", 7)
hinh_tam_giac = Triangle("Hình tam giác", 10, 8)
shapes = [hinh_chu_nhat, hinh_tron, hinh_tam_giac]

for shape in shapes:
    shape.area()