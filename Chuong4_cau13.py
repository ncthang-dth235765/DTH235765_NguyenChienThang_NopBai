#Câu 13: Hàm kiểm tra số hoàn thiện, số thịnh vượng
def tong_uoc(n):
    """Tính tổng các ước số (không kể chính n)."""
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    return s


def la_hoan_thien(n):
    """Kiểm tra số hoàn thiện."""
    return tong_uoc(n) == n


def la_thinh_vuong(n):
    """Kiểm tra số thịnh vượng."""
    return tong_uoc(n) > n


# --- Chương trình chính ---
n = int(input("Nhập số nguyên dương n: "))

if la_hoan_thien(n):
    print(f"{n} là số hoàn thiện.")
elif la_thinh_vuong(n):
    print(f"{n} là số thịnh vượng.")
else:
    print(f"{n} không phải là số hoàn thiện hay thịnh vượng.")
