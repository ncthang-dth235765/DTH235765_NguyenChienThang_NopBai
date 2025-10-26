#Câu 12: Xử lý CSV File - Viết phần mềm Quản Lý Nhân Viên
import csv
import random

# Hàm tạo file CSV gồm 10 dòng, mỗi dòng có 10 số ngẫu nhiên (0-100)
def tao_file_csv(filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=';')
        for _ in range(10):  # 10 dòng
            dong = [random.randint(0, 100) for _ in range(10)]  # 10 số mỗi dòng
            writer.writerow(dong)
    print("✅ Đã tạo file CSV thành công:", filename)


# Hàm đọc file CSV và xuất tổng của mỗi dòng
def doc_file_csv(filename):
    with open(filename, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        dong_so = 1
        for row in reader:
            # Chuyển các phần tử từ chuỗi sang số nguyên
            numbers = [int(x) for x in row if x.strip() != '']
            print(f"Tổng dòng {dong_so}: {sum(numbers)}")
            dong_so += 1


# --- Chạy chương trình ---
file_name = "random_numbers.csv"

tao_file_csv(file_name)
doc_file_csv(file_name)
