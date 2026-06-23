class book:
    def __init__(self, ten_sach, ten_tg, so_chuong):
        self.ten_sach = ten_sach
        self.ten_tg = ten_tg
        self.so_chuong = so_chuong
    def show_info(self):
        print(f'Tên sách: {self.ten_sach} của tác giả: {self.ten_tg} - Số chương: {self.so_trang}')
book_1 = book("Cổ Chân Nhân", "Cổ Chân Nhân", 3381)
book_2 = book("Tiên Nghịch", "Nhĩ Căn", 2088)
book_3 = book("Ta mô phỏng trường sinh lộ", "Phẫn Nộ Đích Ô Tặc", 1782)
books = [book_1, book_2, book_3]
stt = 1
for book in books:
    book.show_info()