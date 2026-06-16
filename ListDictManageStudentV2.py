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
        name = input("Nhập tên học sinh: ")
        try:
            score = float(input("Nhập điểm học sinh: "))
        except ValueError:
            print("Điểm phải là số")
            continue
        if score < 0 or score > 10:
            print("Điểm không hợp lệ. Vui lòng nhập lại.")
            continue
        students.append({"name": name, "score": score})
        print("Học sinh đã được thêm thành công.")
    elif choice == "2":
        print("Danh sách học sinh:")
        if not students:
            print("Danh sách rỗng")
        else:
            for student in students:
                print('Tên: ' + student["name"] + ' - Điểm:' + str(student["score"]))
    elif choice == "3":
        name = input("Nhập tên học sinh cần tìm: ")
        name = name.lower().strip()
        found = False
        for student in students:
            found_student = student["name"].lower()
            if name in found_student:
                print("Tên: " + student["name"] + " - Điểm: " + str(student["score"]))
                found = True
        if not found:
            print("Không tìm thấy học sinh")
    elif choice == "4":
        name = input("Nhập họ và tên học sinh cần xóa:")
        name = name.lower()
        found = False
        name_del = None
        for student in students:
            student_del = student["name"].lower()
            if name == student_del:
                name_del = student
                found = True
                break
        if not found:
            print("Học sinh không tồn tại")
        if name_del:
            students.remove(name_del)
            print("Học sinh đã bị xóa")
    elif choice == "5":
        print("Cảm ơn đã xài chương trình")
        break