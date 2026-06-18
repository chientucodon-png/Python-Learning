while True:
    print("Lựa chọn chức năng:")
    print("1. Thêm công việc")
    print("2. Xem danh sách công việc")
    print("3. Xóa việc khỏi danh sách")
    print("4. Thoát")
    choice = input("Nhập lựa chọn của bạn:")
    if choice == "1":
        cv = input("Nhập công việc muốn thêm:")
        with open('todo.txt', 'a', encoding='utf-8') as f: 
            f.write(f'\n{cv.strip()}')
        print("Thêm cv thành công!")
    elif choice == "2":
        with open('todo.txt', 'r', encoding='utf-8') as f:
            dong = 1
            print(f'Danh sách bây giờ là:')
            for cv in f:
                print(f'{dong}. {cv.strip()}')
                dong += 1
    elif choice == "3":
        xoa = input("Bạn muốn xóa công việc ở dòng mấy?")
        with open('todo.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
            dong = int(xoa)
            if 1 <= dong <= len(lines):
                del lines[dong - 1]
                with open('todo.txt', 'w', encoding='utf-8') as f:
                    f.writelines(lines)
                print("Đã xóa")
            else:
                print("Dòng không hợp lệ")
    elif choice == "4":
        print('Cảm ơn đã xài chương trình.')
        break