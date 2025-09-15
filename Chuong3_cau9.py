#Câu 9: Nhập vào 1 tháng, xuất ra tháng đó thuộc quý mấy trong năm.
thang = int(input("Nhập tháng (1-12): "))
if 1 <= thang <= 3:
    quy = 1
elif 4 <= thang <= 6:
    quy = 2
elif 7 <= thang <= 9:
    quy = 3
elif 10 <= thang <= 12:
    quy = 4
else:
    quy = None

if quy:
    print(f"Tháng {thang} thuộc quý {quy} trong năm.")
else:
    print("Tháng không hợp lệ! Vui lòng nhập số từ 1 đến 12.")
