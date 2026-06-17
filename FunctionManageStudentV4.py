def hien_thi_hs(ds, key_name = "name", key_score = "score"):
    #tự truyền key
    #mặc định là key_name = "name" và key_score = "score"
    if not ds:
        print("Danh sách rỗng")
        return
    if key_name not in ds[0]:
        print("Key name chưa đúng")
        print(f'Các key hiện tại: {list(ds[0].keys())}')
        return
    if key_score not in ds[0]:
        print("Key score chưa đúng")
        print(f'Các key hiện tại: {list(ds[0].keys())}')
        return
    for student in ds:
        ten = student[key_name]
        diem = student[key_score]
        print(f'{ten}')
        for subject, score in diem.items():
            print(f'{subject} {score}')
def tinh_diem_tb(ds, key_name = "name", key_score = "score"):
    #tự truyền key
    #mặc định là key_name = "name" và key_score = "score"
    if not ds:
        print("Danh sách rỗng")
        return
    if key_name not in ds[0]:
        print("Key name chưa đúng")
        print(f'Các key hiện tại: {list(ds[0].keys())}')
        return
    if key_score not in ds[0]:
        print("Key score chưa đúng")
        print(f'Các key hiện tại: {list(ds[0].keys())}')
        return
    for student in ds:
        ten = student[key_name]
        diem = student[key_score].values()
        diem_tb = sum(diem) / len(diem)
        print(f'{ten}')
        print(f'Điểm trung bình: {diem_tb}')
def diem_cao_nhat(ds, key_name = "name", key_score = "score"):
    #tự truyền key
    #mặc định là key_name = "name" và key_score = "score"
    if not ds:
        print("Danh sách rỗng")
        return
    if key_name not in ds[0]:
        print("Key name chưa đúng")
        print(f'Các key hiện tại: {list(ds[0].keys())}')
        return
    if key_score not in ds[0]:
        print("Key score chưa đúng")
        print(f'Các key hiện tại: {list(ds[0].keys())}')
        return
    cac_mon = list(ds[0][key_score].keys())
    for mon in cac_mon:
        diem_cao_nhat = -1
        ten_hs = ""
        for student in ds:
            diem_hien_tai = student[key_score][mon]
            if diem_hien_tai > diem_cao_nhat:
                diem_cao_nhat = diem_hien_tai
                ten_hs = student[key_name]
        print(f'Điểm cao nhất môn {mon} là: {ten_hs} với {diem_cao_nhat} điểm')
def dem_hs(ds, key_name = "name", key_score = "score"):
    #tự truyền key
    #mặc định là key_name = "name" và key_score = "score"
    if not ds:
        print("Danh sách rỗng")
        return
    if key_name not in ds[0]:
        print("Key name chưa đúng")
        print(f'Các key hiện tại: {list(ds[0].keys())}')
        return
    if key_score not in ds[0]:
        print("Key score chưa đúng")
        print(f'Các key hiện tại: {list(ds[0].keys())}')
        return
    print(f'Số lượng học sinh trong lớp là: {len(ds)}')
students = [
    {
        "name": "Nguyen Van A",
        "score": {
            "math":9.0,
            "english": 8.0,
            "physics": 9.5
        }
    },
    {
        "name": "Tran Thi B",
        "score": {
            "math":4.0,
            "english": 10.0,
            "physics": 4.5
        }
    },
    {
        "name": "Le Van A",
        "score": {
            "math":10.0,
            "english": 2.0,
            "physics": 10.0
        }
    }
]
while True:
    print("Danh sách chức năng")
    print("1. Hiển thị danh sách")
    print("2. Điểm trung bình mỗi học sinh")
    print("3. Học sinh có điểm cao nhất")
    print("4. Số lượng học sinh trong lớp")
    print("5. Thoát")
    choice = input("Nhập lựa chọn của bạn:")
    if choice == "1":
        hien_thi_hs(students)
    elif choice == "2":
        tinh_diem_tb(students)
    elif choice == "3":
        diem_cao_nhat(students)
    elif choice == "4":
        dem_hs(students)
    elif choice == "5":
        print("Cảm ơn vì đã sử dụng chương trình!")
        break