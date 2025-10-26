#Câu 3: Xử lý List Đa chiều
from random import randrange

# --- Hàm tạo ma trận m x n ngẫu nhiên ---
def TaoMaTran(m, n):
    D = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(randrange(100))
        D.append(row)
    return D

# --- Hàm xuất ma trận ---
def XuatMaTran(D):
    for row in D:
        for element in row:
            print(element, end='\t')
        print()

# --- Hàm lấy dòng r ---
def LayDong(D, r):
    return D[r]

# --- Hàm xuất list 1 chiều ---
def XuatList1Chieu(R):
    for element in R:
        print(element, end='\t')
    print()

# --- Hàm lấy cột c ---
def LayCot(D, c):
    C = []
    for i in range(len(D)):
        C.append(D[i][c])
    return C

# --- Hàm tìm giá trị lớn nhất trong ma trận ---
def MAX(D):
    max_val = D[0][0]
    for i in range(len(D)):
        for j in range(len(D[i])):
            if max_val < D[i][j]:
                max_val = D[i][j]
    return max_val

# --- Chương trình chính ---
m = int(input("Nhập số dòng: "))
n = int(input("Nhập số cột: "))

D = TaoMaTran(m, n)
print("Ma trận vừa tạo là:")
XuatMaTran(D)

r = int(input("Nhập chỉ số dòng cần lấy (0..m-1): "))
dong = LayDong(D, r)
print("Dòng", r, "là:")
XuatList1Chieu(dong)

c = int(input("Nhập chỉ số cột cần lấy (0..n-1): "))
cot = LayCot(D, c)
print("Cột", c, "là:")
XuatList1Chieu(cot)

print("Giá trị lớn nhất trong ma trận là:", MAX(D))
