#Câu 7: Trình bày một số cách nhập dữ liệu từ bàn phím.
'''
- Nhập dữ liệu dưới dạng chuỗi (mặc định):
name = input("Nhập tên của bạn: ")
print("Xin chào", name)

- Chuyển dữ liệu nhập vào thành số nguyên:
age = int(input("Nhập tuổi của bạn: "))
print("Tuổi bạn là", age)

- Chuyển dữ liệu nhập vào thành số thực:
height = float(input("Nhập chiều cao của bạn: "))
print("Chiều cao bạn là", height)

- Nhập nhiều giá trị trên cùng một dòng (cách thông dụng với tách chuỗi):
a, b = input("Nhập hai số, cách nhau bằng dấu cách: ").split()
a = int(a)
b = int(b)
print("Tổng hai số là", a + b)

'''