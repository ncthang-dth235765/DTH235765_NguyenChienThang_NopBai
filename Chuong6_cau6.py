#Câu 6: Nhập vào 1 list có N số ngẫu nhiên KHÔNG TRÙNG NHAU
import random

print("Nhập số phần tử N:")
N = int(input())

# Lấy N số ngẫu nhiên KHÔNG TRÙNG từ khoảng 0–99
lst = random.sample(range(0, 100), N)

print("List ngẫu nhiên (không trùng nhau):")
print(lst)
