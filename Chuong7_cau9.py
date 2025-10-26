#Câu 9: Xử lý Text File - Viết phần mềm Quản Lý sản phẩm
'''
File lưu dữ liệu (sanpham.txt)

SP1;Coca;15000;DM1
SP2;Pepsi;18000;DM1
SP3;Oreo;12000;DM2
'''
# ==============================
# CHƯƠNG TRÌNH QUẢN LÝ SẢN PHẨM
# ==============================

import os

# ------------------------------
# KHAI BÁO LỚP DỮ LIỆU
# ------------------------------
class DanhMuc:
    def __init__(self, ma, ten):
        self.ma = ma
        self.ten = ten

class SanPham:
    def __init__(self, ma, ten, dongia, madm):
        self.ma = ma
        self.ten = ten
        self.dongia = dongia
        self.madm = madm  # mã danh mục


# ------------------------------
# CÁC HÀM XỬ LÝ
# ------------------------------

def LuuFile(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        for line in data:
            f.write(line + '\n')


def DocFile(path):
    if not os.path.exists(path):
        return []
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.read().splitlines()
    return lines


# ------------------------------
# HÀM CHÍNH CHO DANH MỤC & SẢN PHẨM
# ------------------------------

def ThemDanhMuc(dsdm):
    ma = input("Nhập mã danh mục: ")
    ten = input("Nhập tên danh mục: ")
    dsdm.append(DanhMuc(ma, ten))
    print("✅ Thêm danh mục thành công!")


def ThemSanPham(dssp, dsdm):
    ma = input("Nhập mã sản phẩm: ")
    ten = input("Nhập tên sản phẩm: ")
    dongia = float(input("Nhập đơn giá: "))
    madm = input("Nhập mã danh mục: ")
    # kiểm tra tồn tại danh mục
    if any(dm.ma == madm for dm in dsdm):
        dssp.append(SanPham(ma, ten, dongia, madm))
        print("✅ Thêm sản phẩm thành công!")
    else:
        print("❌ Mã danh mục không tồn tại!")


def XuatDanhSachSanPham(dssp):
    print("\n{:<10}{:<20}{:<15}{:<10}".format("Mã", "Tên sản phẩm", "Đơn giá", "Mã DM"))
    print("-" * 55)
    for sp in dssp:
        print("{:<10}{:<20}{:<15,.0f}{:<10}".format(sp.ma, sp.ten, sp.dongia, sp.madm))
    print()


def TimKiemSanPham(dssp):
    keyword = input("Nhập tên hoặc mã sản phẩm cần tìm: ").lower()
    kq = [sp for sp in dssp if keyword in sp.ten.lower() or keyword in sp.ma.lower()]
    if not kq:
        print("❌ Không tìm thấy sản phẩm!")
    else:
        XuatDanhSachSanPham(kq)


def XoaSanPham(dssp):
    ma = input("Nhập mã sản phẩm cần xóa: ")
    for sp in dssp:
        if sp.ma == ma:
            dssp.remove(sp)
            print("✅ Đã xóa sản phẩm", ma)
            return
    print("❌ Không tìm thấy mã sản phẩm.")


def SuaSanPham(dssp):
    ma = input("Nhập mã sản phẩm cần sửa: ")
    for sp in dssp:
        if sp.ma == ma:
            sp.ten = input("Nhập tên mới: ")
            sp.dongia = float(input("Nhập đơn giá mới: "))
            print("✅ Đã cập nhật sản phẩm!")
            return
    print("❌ Không tìm thấy sản phẩm cần sửa.")


def SapXepSanPham(dssp):
    dssp.sort(key=lambda sp: sp.dongia, reverse=True)
    print("✅ Đã sắp xếp theo đơn giá giảm dần.")


def LuuDuLieu(dssp, file):
    data = [f"{sp.ma};{sp.ten};{sp.dongia};{sp.madm}" for sp in dssp]
    LuuFile(file, data)
    print("💾 Đã lưu dữ liệu vào file.")


def DocDuLieu(file):
    lines = DocFile(file)
    dssp = []
    for line in lines:
        if line.strip():
            ma, ten, dongia, madm = line.split(";")
            dssp.append(SanPham(ma, ten, float(dongia), madm))
    return dssp


# ------------------------------
# CHƯƠNG TRÌNH CHÍNH
# ------------------------------

def main():
    dsdm = [DanhMuc("DM1", "Nước giải khát"), DanhMuc("DM2", "Bánh kẹo")]
    dssp = DocDuLieu("sanpham.txt")

    while True:
        print("\n=== QUẢN LÝ SẢN PHẨM ===")
        print("1. Thêm danh mục")
        print("2. Thêm sản phẩm")
        print("3. Xuất danh sách sản phẩm")
        print("4. Tìm kiếm sản phẩm")
        print("5. Xóa sản phẩm")
        print("6. Sửa sản phẩm")
        print("7. Sắp xếp theo giá giảm dần")
        print("8. Lưu file")
        print("9. Thoát")
        chon = input("Chọn chức năng: ")

        if chon == "1":
            ThemDanhMuc(dsdm)
        elif chon == "2":
            ThemSanPham(dssp, dsdm)
        elif chon == "3":
            XuatDanhSachSanPham(dssp)
        elif chon == "4":
            TimKiemSanPham(dssp)
        elif chon == "5":
            XoaSanPham(dssp)
        elif chon == "6":
            SuaSanPham(dssp)
        elif chon == "7":
            SapXepSanPham(dssp)
        elif chon == "8":
            LuuDuLieu(dssp, "sanpham.txt")
        elif chon == "9":
            print("👋 Tạm biệt!")
            break
        else:
            print("❌ Lựa chọn không hợp lệ!")


if __name__ == "__main__":
    main()
