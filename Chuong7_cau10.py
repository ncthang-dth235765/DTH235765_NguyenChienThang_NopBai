#Câu 10: Xử lý JSON File - Viết phần mềm Quản Lý Sinh Viên
import json
import os
'''
Cấu trúc file JSON (sinhvien.json)
[
    {
        "ma": "SV01",
        "ten": "Nguyễn Văn A",
        "namsinh": "2003",
        "malop": "CTK46"
    },
    {
        "ma": "SV02",
        "ten": "Trần Thị B",
        "namsinh": "2004",
        "malop": "QTKD45"
    }
]

'''

# ==============================
# 1️⃣ ĐỊNH NGHĨA LỚP DỮ LIỆU
# ==============================
class Lop:
    def __init__(self, ma, ten):
        self.ma = ma
        self.ten = ten


class SinhVien:
    def __init__(self, ma, ten, namsinh, malop):
        self.ma = ma
        self.ten = ten
        self.namsinh = namsinh
        self.malop = malop


# ==============================
# 2️⃣ HÀM XỬ LÝ FILE JSON
# ==============================
def LuuFileJSON(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print("💾 Đã lưu dữ liệu vào file JSON!")


def DocFileJSON(path):
    if not os.path.exists(path):
        return []
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


# ==============================
# 3️⃣ HÀM XỬ LÝ CHỨC NĂNG
# ==============================
def ThemLop(ds_lop):
    ma = input("Nhập mã lớp: ")
    ten = input("Nhập tên lớp: ")
    ds_lop.append(Lop(ma, ten))
    print("✅ Thêm lớp thành công!")


def ThemSinhVien(ds_sv, ds_lop):
    ma = input("Nhập mã sinh viên: ")
    ten = input("Nhập tên sinh viên: ")
    namsinh = input("Nhập năm sinh: ")
    malop = input("Nhập mã lớp: ")

    # kiểm tra mã lớp tồn tại
    if not any(l.ma == malop for l in ds_lop):
        print("❌ Mã lớp không tồn tại!")
        return

    ds_sv.append(SinhVien(ma, ten, namsinh, malop))
    print("✅ Thêm sinh viên thành công!")


def XuatDanhSachSV(ds_sv):
    print("\n{:<10}{:<25}{:<15}{:<10}".format("Mã SV", "Tên sinh viên", "Năm sinh", "Mã lớp"))
    print("-" * 60)
    for sv in ds_sv:
        print("{:<10}{:<25}{:<15}{:<10}".format(sv.ma, sv.ten, sv.namsinh, sv.malop))
    print()


def TimKiemSinhVien(ds_sv):
    keyword = input("Nhập mã hoặc tên sinh viên cần tìm: ").lower()
    kq = [sv for sv in ds_sv if keyword in sv.ten.lower() or keyword in sv.ma.lower()]
    if kq:
        XuatDanhSachSV(kq)
    else:
        print("❌ Không tìm thấy sinh viên!")


def XoaSinhVien(ds_sv):
    ma = input("Nhập mã sinh viên cần xóa: ")
    for sv in ds_sv:
        if sv.ma == ma:
            ds_sv.remove(sv)
            print("✅ Đã xóa sinh viên", ma)
            return
    print("❌ Không tìm thấy sinh viên.")


def SuaSinhVien(ds_sv):
    ma = input("Nhập mã sinh viên cần sửa: ")
    for sv in ds_sv:
        if sv.ma == ma:
            sv.ten = input("Nhập tên mới: ")
            sv.namsinh = input("Nhập năm sinh mới: ")
            sv.malop = input("Nhập mã lớp mới: ")
            print("✅ Cập nhật thông tin thành công!")
            return
    print("❌ Không tìm thấy sinh viên.")


def SapXepSinhVien(ds_sv):
    ds_sv.sort(key=lambda sv: sv.ten.lower())
    print("✅ Đã sắp xếp sinh viên theo tên A→Z.")


def LuuDuLieu(ds_sv, path):
    data = []
    for sv in ds_sv:
        data.append({
            "ma": sv.ma,
            "ten": sv.ten,
            "namsinh": sv.namsinh,
            "malop": sv.malop
        })
    LuuFileJSON(path, data)


def DocDuLieu(path):
    ds_sv = []
    data = DocFileJSON(path)
    for item in data:
        ds_sv.append(SinhVien(item["ma"], item["ten"], item["namsinh"], item["malop"]))
    return ds_sv


# ==============================
# 4️⃣ MENU CHÍNH
# ==============================
def main():
    ds_lop = [Lop("CTK46", "Công nghệ thông tin K46"), Lop("QTKD45", "Quản trị kinh doanh K45")]
    ds_sv = DocDuLieu("sinhvien.json")

    while True:
        print("\n=== QUẢN LÝ SINH VIÊN ===")
        print("1. Thêm lớp")
        print("2. Thêm sinh viên")
        print("3. Xuất danh sách sinh viên")
        print("4. Tìm kiếm sinh viên")
        print("5. Xóa sinh viên")
        print("6. Sửa sinh viên")
        print("7. Sắp xếp sinh viên theo tên")
        print("8. Lưu file JSON")
        print("9. Thoát")
        chon = input("👉 Chọn chức năng: ")

        if chon == "1":
            ThemLop(ds_lop)
        elif chon == "2":
            ThemSinhVien(ds_sv, ds_lop)
        elif chon == "3":
            XuatDanhSachSV(ds_sv)
        elif chon == "4":
            TimKiemSinhVien(ds_sv)
        elif chon == "5":
            XoaSinhVien(ds_sv)
        elif chon == "6":
            SuaSinhVien(ds_sv)
        elif chon == "7":
            SapXepSinhVien(ds_sv)
        elif chon == "8":
            LuuDuLieu(ds_sv, "sinhvien.json")
        elif chon == "9":
            print("👋 Tạm biệt!")
            break
        else:
            print("❌ Lựa chọn không hợp lệ!")


if __name__ == "__main__":
    main()
