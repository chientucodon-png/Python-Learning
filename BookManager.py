import json

def tai_du_lieu(ten_file):
    with open(ten_file, 'r', encoding='utf-8') as f:
        return json.load(f)
    
def them_sach(ds):
        ten_sach = input('Nhập tên sách:')
        ten_tac_gia = input('Nhập tên tác giả:')
        so_trang = input('Nhập số trang sách:')
        ds.append({
            "ten_sach": ten_sach,
            "ten_tac_gia": ten_tac_gia,
            "so_trang": so_trang
        })

def hien_thi_sach(ds,key_book_name = "ten_sach", key_human_name = "ten_tac_gia", key_number= "so_trang", ten_file = "books.json"):
    stt = 1
    for sach in ds:
        print(f'{stt}. Tên sách: {sach.get(key_book_name)}')
        print(f'       Tên tác giả: {sach.get(key_human_name)}')
        print(f'       Số trang: {sach.get(key_number)}')
        stt += 1

def tim_sach(ds,key_book_name = "ten_sach", key_human_name = "ten_tac_gia", key_number= "so_trang"):
    tim = input("Nhập tên sách muốn tìm:")
    tim = tim.lower().strip()
    found = False
    for sach in ds:
        if tim == sach.get(key_book_name).lower().strip():
            print(f'Tên sách: {sach.get(key_book_name)}')
            print(f'Tên tác giả: {sach.get(key_human_name)}')
            print(f'Số trang: {sach.get(key_number)}')
            found = True
    if not found:
        print("Không tìm thấy sách")

def tinh_tong(ds, key_number = "so_trang"):
    tong = 0
    for sach in ds:
        tong = tong + int(sach.get(key_number))
    print(f'Tổng số trang là: {tong}')

def luu_json(ds, ten_file = "books.json"):
    with open(ten_file, 'w', encoding='utf-8') as f:
        json.dump(ds, f, indent = 4, ensure_ascii= False)
        return

books = tai_du_lieu('books.json')
while True:
    print("Danh sách các chức năng")
    print("1. Thêm sách mới")
    print("2. Hiển thị toàn bộ sách")
    print("3. Tìm sách theo tên")
    print("4. Tính tổng số trang")
    print("5. Lưu JSON")
    print("6. Tải JSON")
    print("7. Thoát")
    choice = input('Nhập lựa chọn của bạn:')
    if choice == '1':
        them_sach(books)
    elif choice == '2':
        hien_thi_sach(books)
    elif choice == '3':
        tim_sach(books)
    elif choice == '4':
        tinh_tong(books)
    elif choice == '5':
        luu_json(books)
    elif choice == '6':
        books = tai_du_lieu('books.json')
    elif choice == '7':
        print("Cảm ơn vì đã sử dụng chương trình!")
        break