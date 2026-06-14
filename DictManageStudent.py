student = {
    "name": "Nguyen Van A",
    "age": 20,
    "score": 8.5,
    "gender":"male",
    "class":"12A1"

}
while True:
    print("Đây là chương trình quản lý học sinh, vui lòng chọn chức năng:")
    print("1. Xem thông tin")
    print("2. Sửa tuổi")
    print("3. Thêm điểm")
    print("4. Xóa điểm")
    print("5. Thoát")
    choice = input("Nhập lựa chọn của bạn:")
    if choice == "1":
        print("Thông tin học sinh:")
        for key,value in student.items():
            if value is None and key == "score":
                print(key, ": chưa có điểm")
            else:
                print(key, ":", value)
    elif choice == "2":
        print("Tuổi hiện tại của " + student["name"] + " là " + str(student["age"]))
        try:
            new_age = input("Nhập tuổi mới:")
            if int(new_age) <= 0:
                print("Tuổi phải là một số nguyên dương, vui lòng nhập lại.")
                continue
            student["age"] = int(new_age)
        except ValueError:
            print("Tuổi phải là một số nguyên, vui lòng nhập lại.")
            continue
        print("Tuổi đã được cập nhật, tuổi hiện tại của " + student["name"] + " là " + str(student["age"]))
    elif choice == "3":
        try:
            new_score = input("Thêm điểm mới:")
            if float(new_score) < 0 or float(new_score) > 10:
                print("Điểm phải nằm trong khoảng từ 0 đến 10, vui lòng nhập lại.")
                continue
            student["score"] = float(new_score)
            print("Điểm đã được thêm, điểm hiện tại của " + student["name"] + " là " + str(student["score"]))
        except ValueError:
            print("Điểm phải là một số, vui lòng nhập lại.")
            continue
    elif choice == "4":
        if student["score"] is not None:
            student["score"] = None
            print("Điểm đã được xóa.")
        else:
            print("Học sinh chưa có điểm để xóa.")
    elif choice == "5":
        print("Cảm ơn bạn đã sử dụng chương trình!")
        break
    else:
        print("Lựa chọn không hợp lệ, vui lòng chọn lại.")