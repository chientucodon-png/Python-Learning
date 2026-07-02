#bài 1 packing và cú pháp cơ bản

numbers = 10, 20, 30, 40, 50
print(numbers[0])
print(numbers[-1])
print(len(numbers))

#bài 2 unpacking

person = ("An",18,"Đà Nẵng")

name, age, city = person

print(name)
print(age)
print(city)

#bài 3 lấy toàn bộ giá trị trong tuple

numbers = (5,8,10,15,20)

for number in numbers:
    print(number)

#bài 4 cú pháp đếm và tìm chỉ số

numbers = (1,2,2,2,3,4)

print(numbers.count(2))
print(numbers.index(3))

#bài 5 đổi giá trị biến

a = 300
b = 500

a, b = b, a

print(a, b)

#bài 6 tuple làm key của dict

point = {}
point[(20, 10)] = "Nhà"
print(point[20, 10])
