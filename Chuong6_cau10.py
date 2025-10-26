#Câu 10: Xử lý Ma Trận
# === Hàm nhập ma trận ===
def NhapMaTran(ten):
    print(f"Nhập số dòng của ma trận {ten}: ", end="")
    m = int(input())
    print(f"Nhập số cột của ma trận {ten}: ", end="")
    n = int(input())

    M = []
    print(f"Nhập các phần tử cho ma trận {ten}:")
    for i in range(m):
        row = []
        for j in range(n):
            x = float(input(f"{ten}[{i}][{j}] = "))
            row.append(x)
        M.append(row)
    return M

# === Hàm xuất ma trận ===
def XuatMaTran(M, ten):
    print(f"\nMa trận {ten}:")
    for row in M:
        for val in row:
            print(f"{val:8.2f}", end=" ")
        print()

# === Hàm cộng hai ma trận ===
def CongMaTran(A, B):
    m = len(A)
    n = len(A[0])
    C = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(A[i][j] + B[i][j])
        C.append(row)
    return C

# === Hàm hoán vị ma trận (transpose) ===
def HoanVi(M):
    m = len(M)
    n = len(M[0])
    T = []
    for j in range(n):
        row = []
        for i in range(m):
            row.append(M[i][j])
        T.append(row)
    return T

# === Chương trình chính ===
A = NhapMaTran("A")
B = NhapMaTran("B")

# Xuất hai ma trận
XuatMaTran(A, "A")
XuatMaTran(B, "B")

# Cộng hai ma trận
if len(A) == len(B) and len(A[0]) == len(B[0]):
    C = CongMaTran(A, B)
    XuatMaTran(C, "A + B")
else:
    print("\n Hai ma trận không cùng kích thước, không thể cộng!")

# Tìm ma trận hoán vị của A và B
TA = HoanVi(A)
TB = HoanVi(B)

XuatMaTran(TA, "Aᵀ (hoán vị của A)")
XuatMaTran(TB, "Bᵀ (hoán vị của B)")
