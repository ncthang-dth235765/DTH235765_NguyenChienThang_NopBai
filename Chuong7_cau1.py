#Câu 1: Quản lý Sản phẩm- Text File
'''
File 1: XuLyFile.py
def LuuFile(path, data):
    with open(path, 'a', encoding='utf-8') as file:
        file.writelines(data)
        file.writelines("\n")


def DocFile(path):
    arrProduct = []
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            data = line.strip()
            if data != "":
                arr = data.split(';')
                arrProduct.append(arr)
    return arrProduct

File 2: TestLuuFile.py
from XuLyFile import *

masp = input("Nhập mã SP: ")
tensp = input("Nhập tên SP: ")
dongia = float(input("Nhập đơn giá: "))

line = masp + ";" + tensp + ";" + str(dongia)
LuuFile("database.txt", line)

print("✅ Đã lưu sản phẩm vào file database.txt")

File 3: TestDocFile.py
from XuLyFile import *

# Đọc dữ liệu từ file
dssp = DocFile("database.txt")

# Hàm xuất danh sách sản phẩm
def XuatSanPham(dssp):
    for row in dssp:
        for element in row:
            print(element, end='\t')
        print()
    print()

# Hàm sắp xếp sản phẩm theo đơn giá (giảm dần)
def SortSp(dssp):
    n = len(dssp)
    for i in range(n):
        for j in range(i + 1, n):
            a = float(dssp[i][2])
            b = float(dssp[j][2])
            if a < b:
                dssp[i], dssp[j] = dssp[j], dssp[i]

print("📦 Danh sách sản phẩm trong file:")
XuatSanPham(dssp)

SortSp(dssp)

print("📊 Sản phẩm sau khi sắp xếp theo giá giảm dần:")
XuatSanPham(dssp)
'''