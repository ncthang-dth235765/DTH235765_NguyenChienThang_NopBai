#Câu 9: Viết chương trình tính căn bậc 2 lồng nhau
import math

# Nhập số n
n = int(input("Nhập n: "))

# Biến S ban đầu = 0 (sẽ được tính từ trong ra ngoài)
S = 0

# Tính căn bậc 2 lồng nhau từ trong ra ngoài
for i in range(n, 0, -1):
    S = math.sqrt(i + S)

# Xuất kết quả
print("Giá trị S =", S)
