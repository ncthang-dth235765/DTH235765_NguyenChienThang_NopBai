#Câu 1: Xử lý List
from random import randrange

print("Chương trình xử lý List")
n = int(input("Nhập số phần tử: "))

# Tạo list ngẫu nhiên
lst = [randrange(-100, 100) for _ in range(n)]
print("List ngẫu nhiên là:")
print(lst)

# Thêm 1 số mới
value = int(input("Mời bạn thêm số mới: "))
lst.append(value)
print("List sau khi thêm:", lst)

# Đếm số xuất hiện
k = int(input("Bạn muốn đếm số nào: "))
dem = lst.count(k)
print(k, "xuất hiện", dem, "lần trong list")

# ---- Hàm kiểm tra số nguyên tố ----
def CheckPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# ---- Đếm và tính tổng các số nguyên tố ----
demnt = 0
tongnt = 0
for x in lst:
    if CheckPrime(x):
        demnt += 1
        tongnt += x

print("Có", demnt, "số nguyên tố trong list")
print("Tổng các số nguyên tố =", tongnt)

# ---- Sắp xếp list tăng dần ----
lst.sort()
print("List sau khi sort:", lst)

# ---- Xóa list ----
del lst
try:
    print("List sau khi xóa:", lst)
except NameError:
    print("List đã bị xóa khỏi bộ nhớ!")
