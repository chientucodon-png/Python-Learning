#bài 1

class cat:
    def __init__(self, ten,tuoi):
        self.ten = ten
        self.tuoi = tuoi
    def hello(self):
        print(f'Chào mấy em, anh là {self.ten}')
cat_1 = cat("Mèo Tom", 7)
cat_2 = cat("Mèo béo", 5)
print(f'{cat_1.ten}, {cat_1.tuoi}')
cat_1.hello()

#bài 2

class book:
    def __init__(self, ten_sach, ten_tg, so_trang):
        self.ten_sach = ten_sach
        self.ten_tg = ten_tg
        self.so_trang = so_trang

book_1 = book("Minh Nguyệt", "Ái Khả Nhĩ", 350)
book_2 = book("Song Phượng Lân", "Ái Minh Minh", 252)
book_3 = book("Đạm Minh Đài", "Thảo Khấu Quốc", 950)
books = [book_1, book_2, book_3]
stt = 1
for book in books:
    print(f'Cuốn sách {stt}')
    print(f'    Tên sách: {book.ten_sach}')
    print(f'    Tên tác giả: {book.ten_tg}')
    print(f'    Số trang: {book.so_trang}')
    stt += 1

#bài 3

class student:
    def __init__(self, ten, diem, toan, ly, hoa):
        self.ten = ten
        self.diem = diem
        self.toan = toan
        self.ly = ly
        self.hoa = hoa
    #bài 4
    def show_info(self):
        print(f'    Tên: {self.ten}\n    Điểm: {self.diem}')
    #bài 5
    def check_pass(self):
        if self.diem >= 5:
            print(f'Học sinh {self.ten} đậu')
        else:
            print(f'Học sinh {self.ten} rớt')
    #bải 6
    def tinh_diem_tb(self):
        diem_tb = (self.toan + self.ly + self.hoa) / 3
        print(f'Điểm trung bình của {self.ten} là {diem_tb:.2f}')
student_1 = student("An", 8,10,9,8)
student_2 = student("Minh", 5, 5,6,7)
student_3 = student("Hong", 10, 8, 9, 9)
students = [student_1, student_2, student_3]
stt = 1
for student in students:
    print(f'Học sinh {stt}')
    print(f'    Tên: {student.ten}')
    print(f'    Điểm: {student.diem}')
    stt += 1
stt = 1
for student in students:
    print(f"Học sinh {stt}:")
    student.show_info()
    stt += 1
student_1.check_pass()
student_2.check_pass()
student_3.check_pass()
student_1.tinh_diem_tb()
student_2.tinh_diem_tb()
student_3.tinh_diem_tb()
#for book với for student là bài 7