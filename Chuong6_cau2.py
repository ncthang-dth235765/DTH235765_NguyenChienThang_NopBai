#Câu 2: Xử lý List nhập ngẫu nhiên
from random import randrange

# --- Tạo list ngẫu nhiên ---
lst = []
print("Nhập số phần tử:")
n = int(input())

for i in range(n):
    lst.append(randrange(0, 100))

print("List sau khi tạo ngẫu nhiên là:")
print(lst)

# --- Thêm phần tử mới ---
x = int(input("Mời bạn chèn thêm số mới: "))
lst.append(x)
print("List sau khi chèn:")
print(lst)

# --- Xóa tất cả các phần tử bằng k ---
k = int(input("Mời nhập số để xóa: "))
while lst.count(k) > 0:
    lst.remove(k)
print("List sau khi xóa:")
print(lst)

# --- Hàm kiểm tra list đối xứng ---
def CheckDoiXung(lst):
    for i in range(len(lst)):
        if lst[i] != lst[len(lst) - i - 1]:
            return False
    return True

# --- Kiểm tra và xuất kết quả ---
kt = CheckDoiXung(lst)
if kt:
    print("List đối xứng")
else:
    print("List không đối xứng")
