#Câu 7: Viết chương trình nhập vào một dãy các số theo thứ tự tăng, nếu nhập sai quy cách thì yêu cầu nhập lại. In dãy số sau khi đã nhập xong
print("Nhập số phần tử của dãy:")
n = int(input())

lst = []

print("Nhập các số theo thứ tự tăng dần:")

for i in range(n):
    while True:
        x = int(input(f"Nhập số thứ {i+1}: "))
        if i == 0 or x > lst[i-1]:
            lst.append(x)
            break
        else:
            print(" Sai quy tắc! Số phải lớn hơn số trước đó. Nhập lại!")

print("\n Dãy số hợp lệ là:")
print(lst)
