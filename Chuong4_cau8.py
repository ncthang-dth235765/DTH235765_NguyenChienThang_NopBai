#Câu 8: Viết chương trình tính loga
import math

# Nhập a và x từ bàn phím
a = float(input("Nhập cơ số a: "))
x = float(input("Nhập số x: "))

# Kiểm tra điều kiện hợp lệ
if a > 0 and a != 1 and x > 0:
    log_a_x = math.log(x) / math.log(a)
    print("Giá trị log_a(x) =", log_a_x)
else:
    print("Giá trị a và x không hợp lệ! (yêu cầu: a > 0, a != 1, x > 0)")
