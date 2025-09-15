#Câu 8: Trình bày các loại lỗi khi lập trình và cách bắt lỗi trong Python.
'''
Các loại lỗi:
- Lỗi cú pháp (Syntax Error):
Xảy ra khi viết sai cú pháp Python, ví dụ thiếu dấu : hoặc dấu ngoặc.
Ví dụ:
if x > 5  # thiếu dấu hai chấm
    print(x)

- Lỗi thời gian chạy (Runtime Error):
Xảy ra khi chương trình chạy đến một dòng mã gây lỗi, ví dụ chia cho 0, truy cập phần tử ngoài phạm vi, hoặc lỗi kiểu dữ liệu.
Ví dụ:
print(10 / 0)  # lỗi chia cho 0

- Lỗi logic (Logic Error):
Chương trình chạy không báo lỗi nhưng kết quả không đúng do sai lầm trong thuật toán hoặc ý tưởng.

Cách bắt lỗi trong Python:
Python dùng cấu trúc try-except để xử lý lỗi (bắt ngoại lệ):
try:
    # đoạn mã có thể gây lỗi
    x = int(input("Nhập số: "))
    print(10 / x)
except ZeroDivisionError:
    print("Lỗi: không thể chia cho 0")
except ValueError:
    print("Lỗi: giá trị nhập vào không phải số nguyên")
except Exception as e:
    print("Lỗi khác:", e)

try: đặt đoạn mã cần kiểm tra lỗi
except: bắt các lỗi cụ thể và xử lý
Có thể có nhiều except cho từng loại lỗi
Exception là lớp lỗi tổng quát, bắt mọi lỗi không nằm trong các except trước đó

'''