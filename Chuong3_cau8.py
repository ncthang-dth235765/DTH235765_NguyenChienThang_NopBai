#Câu 8: Nhập vào 2 giá trị a, b và phép toán ‘+’, ‘-’, ‘*’, ‘/’ . Hãy xuất kết quả theo đúng phép toán đã nhập.
# Nhập 2 số
a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
# Nhập phép toán
phep_toan = input("Nhập phép toán (+, -, *, /): ")
# Tính toán và xuất kết quả
if phep_toan == '+':
    ket_qua = a + b
elif phep_toan == '-':
    ket_qua = a - b
elif phep_toan == '*':
    ket_qua = a * b
elif phep_toan == '/':
    if b != 0:
        ket_qua = a / b
    else:
        ket_qua = "Lỗi: Không thể chia cho 0!"
else:
    ket_qua = "Phép toán không hợp lệ!"

print("Kết quả:", ket_qua)
