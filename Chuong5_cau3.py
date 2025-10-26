#Câu 3: Xử lý Tách chuỗi
def CheckPrime(x):
    if x < 2:
        return False
    dem = 0
    for i in range(1, x + 1):
        if x % i == 0:
            dem += 1
    return dem == 2


s = "5;7;8;-2;8;11;-13;9;10"
arr = s.split(';')

sochan = 0
soam = 0
sont = 0
tong = 0

for x in arr:
    number = int(x)
    print(number)

    if number % 2 == 0:
        sochan += 1
    if number < 0:
        soam += 1
    if CheckPrime(number):
        sont += 1

    tong += number

print("Số chẵn =", sochan)
print("Số âm =", soam)
print("Số nguyên tố =", sont)
print("Trung bình =", tong / len(arr))
