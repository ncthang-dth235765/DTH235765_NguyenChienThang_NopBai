#Câu 8: Viết chương trình nhập vào một dãy n số thực M[0], M[1],..., M[n-1], sắp xếp dãy số theo thứ tự giảm dần. Xuất ra dãy số sau khi sắp xếp
print("Nhập số phần tử của dãy:")
n = int(input())

M = []  # khởi tạo list rỗng

for i in range(n):
    x = float(input(f"Nhập M[{i}] = "))
    M.append(x)

print("\nDãy ban đầu:")
print(M)

# Sắp xếp giảm dần
M.sort(reverse=True)

print("\n Dãy sau khi sắp xếp giảm dần:")
print(M)
