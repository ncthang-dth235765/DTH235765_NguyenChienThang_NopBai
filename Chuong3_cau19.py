#Câu 19: Tính giá trị biểu thức S
import math
x=float(input("Nhập x: "))
n=int(input("Nhập n: "))
s=0
for i in range(n+1):
    s+=(x**(2*i+1))/math.factorial(2*i+1)
print(f"Giá trị S(x,n)= {s}")