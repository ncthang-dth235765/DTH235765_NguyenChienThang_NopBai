#Câu 9: Xử lý mảng
def CheckPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print("Nhập số phần tử của mảng:")
n = int(input())

arr = []
for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i+1}: "))
    arr.append(x)

print("\nMảng vừa nhập:")
print(arr)

# Dòng 1: Số lẻ
odd = [x for x in arr if x % 2 != 0]
print("\nDòng 1 - Số lẻ:", odd, "→ Có", len(odd), "số lẻ")

# Dòng 2: Số chẵn
even = [x for x in arr if x % 2 == 0]
print("Dòng 2 - Số chẵn:", even, "→ Có", len(even), "số chẵn")

# Dòng 3: Số nguyên tố
prime = [x for x in arr if CheckPrime(x)]
print("Dòng 3 - Số nguyên tố:", prime)

# Dòng 4: Không phải số nguyên tố
not_prime = [x for x in arr if not CheckPrime(x)]
print("Dòng 4 - Không nguyên tố:", not_prime)
