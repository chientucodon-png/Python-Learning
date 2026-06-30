#bài 1: khai báo cú pháp

class Animal:

    def __init__(self, name):
        self.name = name

class Dog(Animal):
    pass

d1 = Dog("Tim")

print(d1.name)

#bài 2: thêm thuộc tính riêng

class Animal:

    def __init__(self, name):
        self.name = name

class Dog(Animal):

    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

d1 = Dog("Tom", 12)

print(d1.age)

#bài 3: ghi đè

class Animal:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        print('Gâu gâu')

class Dog(Animal):

    def __init__(self, name, age):
        super().__init__(name, age)

    def bark(self):
        print('Woof woof')

d1 = Dog("Fish", 9)

d1.bark()

#bài 4: Tổng hợp

class Animals:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def show_info(self):
        print(f'Tên: {self.name}')
        print(f'Tuổi: {self.age}')

class Dog(Animals):

    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def show_info(self):
        super().show_info()
        print(f'Giống: {self.breed}')

class Cat(Animals):

    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def show_info(self):
        super().show_info()
        print(f'Màu: {self.color}')

d1 = Dog("Jimm", 15, "Corgi")
d1.show_info()
c1 = Cat("Jerry", 10, "Orange")
c1.show_info()