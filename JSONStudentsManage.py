def du_lieu(ten_file = "students.json"):
    import json
    try:
        with open(ten_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("File chưa tồn tại!")
        return []
    
def them_hs(ds, key_name = "name", key_score = "score", ten_file = "students.json"):
    ten = input("Nhập tên học sinh muốn thêm:")
    try:
        diem = float(input("Nhập điểm của học sinh muốn thêm:"))
        if diem < 0 or diem > 10:
            print("Điểm không hợp lệ!")
            return ds
        ds.append({
            key_name: ten,
            key_score: diem
        })
    except ValueError:
        print("Điểm phải là một số!")
        return ds
    return ds

def hien_thi_hs(ds, key_name = "name", key_score = "score", ten_file = "students.json"):
    print("Danh sách học sinh:")
    if not ds:
        print("Danh sách rỗng!")
        return
    for student in ds:
        print(f'Tên: {student.get(key_name)} - Điểm: {student.get(key_score)}')
    
def tinh_diem_tb(ds, key_name = "name", key_score = "score", ten_file = "students.json"):
    score = 0
    for student in ds:
        score = score + float(student.get(key_score))
    try:
        diem_tb = score / len(ds)
        print(f'Điểm trung bình cả lớp là: {diem_tb:.2f}')
    except ZeroDivisionError:
        print("Danh sách rỗng!")
        return ds

def luu_json(ds, key_name = "name", key_score = "score", ten_file = "students.json"):
    print("Danh sách hiện tại là:")
    hien_thi_hs(ds)
    luu = input("Xác định lưu? (y/n):")
    if luu == "y":
        import json
        with open(ten_file, 'w', encoding='utf-8') as f:
            json.dump(ds, f, indent=4, ensure_ascii=False)
        print("Lưu thành công!")
    elif luu == "n":
        return
    else:
        print("Lựa chọn chưa hợp lệ!")
        
students = du_lieu()

while True:
    print("Đây là danh sách các lựa chọn")
    print("1. Thêm học sinh")
    print("2. Hiển thị danh sách")
    print("3. Tính điểm trung bình")
    print("4. Lưu JSON")
    print("5. Tải JSON")
    print("6. Thoát")
    choice = input("Nhập lựa chọn của bạn:")
    if choice == "1":
        students = them_hs(students)
        print("Đã thêm học sinh!")
    elif choice == "2":
       hien_thi_hs(students)
    elif choice == "3":
        tinh_diem_tb(students)
    elif choice == "4":
        luu_json(students)
    elif choice == "5":
        students = du_lieu()
        print("Đã load dữ liệu thành công!")
    elif choice == "6":
        print("Cảm ơn đã sử dụng chương trình!")
        break