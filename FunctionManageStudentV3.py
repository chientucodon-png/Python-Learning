def hienthiHS(danh_sach):
    #Hiển thị danh sách học sinh
    if not danh_sach:
        print("Danh sách rỗng")
    else:
        for student in danh_sach:
            print(f'Tên: {student["name"]} - Điểm: {student["score"]}')
def timkiemHS(danh_sach):
    #Tìm kiếm học sinh trong danh sách
    name = input("Nhập tên học sinh cần tìm:")
    name = name.lower().strip()
    found = False
    for student in danh_sach:
        student_name = student["name"].lower()
        if name in student_name:
            print(f'Tên: {student["name"]} - Điểm: {student["score"]}')
            found = True
    if not found:
        print("Học sinh không tồn tại")
def themHS(danh_sach):
    #Thêm học sinh vào danh sách
    name = input("Nhập tên học sinh:").strip()
    try:
        score = float(input("Nhập điểm học sinh:"))
        if score < 0 or score > 10:
            print("Điểm không hợp lệ, vui lòng nhập lại")
            return
    except ValueError:
        print("Điểm phải là số")
        return
    danh_sach.append({"name": name, "score": score})
    print("Đã thêm thành công học sinh")
def xoaHS(danh_sach):
    #Xóa học sinh khỏi danh sách
    name = input("Nhập họ và tên học sinh cần xóa:")
    name = name.lower().strip()
    student_del = None
    for student in danh_sach:
        name_del = student["name"].lower()
        if name == name_del:
            student_del = student
            break
    if student is None:
        print("Học sinh không tồn tại")
    if student_del:
        danh_sach.remove(student_del)
        print("Học sinh đã được xóa")
students = [
    {
        "name": "Nguyen Van A",
        "score": 8.5
    },
    {
        "name": "Tran Thi B",
        "score": 7.0
    },
    {
        "name": "Le Van A",
        "score": 9.0
    }
]
while True:
    print("1. Thêm học sinh mới")
    print("2. Hiển thị danh sách học sinh")
    print("3. Tìm học sinh theo tên")
    print("4. Xóa học sinh")
    print("5. Thoát")
    choice = input("Nhập lựa chọn của bạn:")
    if choice == "1":
        themHS(students)
    elif choice == "2":
        hienthiHS(students)
    elif choice == "3":
        timkiemHS(students)
    elif choice == "4":
        xoaHS(students)
    elif choice == "5":
        print("Cảm ơn bạn đã sử dụng chương trình")
        break
    else:
        print("Lựa chọn không hợp lệ!")