class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print('Đã thêm sách thành công!')

    def show_info(self):
        if not self.books:
            print("Thư viện trống")
        else:
            stt = 1
            print('Danh sách sách trong thư viện')
            for book in self.books:
                print(f'{stt}. {book}')
                stt += 1

my_lib = Library()

class Book:

    def __init__(self, ten_sach, tac_gia, so_chuong):
        self.ten_sach = ten_sach
        self.tac_gia = tac_gia
        self.so_chuong = so_chuong

    def __str__(self):
        return f"{self.ten_sach} - {self.tac_gia} - {self.so_chuong} chương"

def them_sach():
    ten_sach = input("Nhập tên sách muốn thêm:")
    tac_gia = input("Nhập tên tác giả:")
    so_chuong = input("Nhập tổng số chương:")
    book = Book(ten_sach, tac_gia, int(so_chuong))
    my_lib.add_book(book)
    print("Đã thêm sách thành công!")
    return my_lib

def show_info():
    my_lib.show_info()

def find_book():
    ten_sach_can_tim = input("Nhập tên sách cần tìm:")
    found = False
    for book in my_lib.books:
        if ten_sach_can_tim in book.ten_sach:
            print(f'Sách cần tìm là {book}')
            found = True
    if not found:
        print("Không tìm thấy sách")

def count_book():
    print(f'Thư viện có {len(my_lib.books)} cuốn sách!')

def tong_so_trang():
    tong = 0
    for book in my_lib.books:
        tong += book.so_chuong
    print(f'Tổng số chương là {tong}')

while True:
    print("Lựa chọn các chức năng sau")
    print("1. Thêm sách")
    print("2. Hiển thị tất cả sách")
    print("3. Tìm sách theo tên")
    print("4. Đếm số sách")
    print("5. Tổng số trang")
    print("6. Thoát")
    choice = input("Nhập lựa chọn của bạn:")
    if choice == "1":
        them_sach()
    elif choice == "2":
        show_info()
    elif choice == "3":
        find_book()
    elif choice == "4":
        count_book()
    elif choice == "5":
        tong_so_trang()
    elif choice == "6":
        print('Cảm ơn đã sử dụng chương trình!')
        break