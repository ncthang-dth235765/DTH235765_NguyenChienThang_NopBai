#Câu 6: Nhập một số n có tối đa 2 chữ số. Hãy cho biết cách đọc ra dạng chữ.(vd: n=35 => Ba mươi lăm, n=5 => năm).def doc_so(n):
def doc_so(n):
    chu_so = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    if n < 10:
        return chu_so[n]
    
    hang_chuc = n // 10
    hang_dv = n % 10
    
    if hang_chuc == 1:
        prefix = "mười"
    else:
        prefix = chu_so[hang_chuc] + " mươi"
    
    # Xử lý hàng đơn vị
    if hang_dv == 0:
        suffix = ""
    elif hang_dv == 1:
        if hang_chuc == 1:
            suffix = " một"
        else:
            suffix = " mốt"
    elif hang_dv == 5:
        if hang_chuc >= 1:
            suffix = " lăm"
        else:
            suffix = " năm"
    else:
        suffix = " " + chu_so[hang_dv]
    
    return prefix + suffix

n = int(input("Nhập số n (0-99): "))
print(doc_so(n))
