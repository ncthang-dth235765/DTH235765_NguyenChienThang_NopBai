#Câu 18: Vẽ các hình dưới đây
#Với n là chiều cao của hình, hãy dựa vào n để Vẽ các hình dưới đây
def h1(n):
    for i in range(n):
        for j in range(n):
            if i==0 or i==n-1 or j==0 or j==n-1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def h2(n):
    for i in range(1,n+1):
        print("  "*(n-i),end="")
        print("* "*i)
def h3(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            if j==1 or j==i :
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
    for i in range(n-1,0,-1):
        print("  "*(n-i),end="")
        for j in range(1,i+1):
            if j==1 or j==i:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
n=int(input("Nhập n:"))
h1(n)
h2(n)
h3(n)