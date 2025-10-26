#Câu 2: Xử lý số trong Text File
'''
Bước 1 – File dữ liệu mẫu: csdl_so.txt

Bạn có thể tạo file thủ công hoặc để chương trình tự sinh.

Ví dụ nội dung file (mỗi dòng là 1 dãy số, cách nhau bởi dấu phẩy):

-5,4,7,9,3,20
5,-4,37,-19,24,-21
15,9,0,-38,-3,15
5,-4,77,-9,3,-7
55,44,27
-50,26

Bước 2 – File XuLyFile.py
def LuuFile(path, data):
    """Ghi dữ liệu vào file"""
    with open(path, 'a', encoding='utf-8') as file:
        file.writelines(data)
        file.writelines("\n")

def DocFile(path):
    """Đọc file và trả về mảng 2 chiều arrSo"""
    arrSo = []
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            data = line.strip()
            if data != "":
                arr = data.split(',')
                arrSo.append(arr)
    return arrSo

 Bước 3 – File TestLuuFile.py
from XuLyFile import *

# --- Ghi dữ liệu mẫu vào file ---
LuuFile("csdl_so.txt", "-5,4,7,9,3,20")
LuuFile("csdl_so.txt", "5,-4,37,-19,24,-21")
LuuFile("csdl_so.txt", "15,9,0,-38,-3,15")
LuuFile("csdl_so.txt", "5,-4,77,-9,3,-7")
LuuFile("csdl_so.txt", "55,44,27")
LuuFile("csdl_so.txt", "-50,26")

Bước 4 – File TestDocFile.py
from XuLyFile import *
arrSo = DocFile("csdl_so.txt")
print(" Dữ liệu đọc từ file:")
print(arrSo)

# --- Xuất các số âm trên mỗi dòng ---
def XuatSoAmTrenMoiDong(arrSo):
    for row in arrSo:
        for element in row:
            number = int(element)
            if number < 0:
                print(number, end='\t')
        print()  # xuống dòng sau mỗi hàng

print("\n Các số âm trên mỗi dòng:")
XuatSoAmTrenMoiDong(arrSo)
'''