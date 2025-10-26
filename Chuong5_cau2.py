#Câu 2: Viết chương trình tối ưu chuỗi
def ToiUuChuoi(s):
    s2 = s.strip()           # bỏ khoảng trắng đầu & cuối
    arr = s2.split(' ')      # tách các phần theo dấu cách
    s2 = ""
    for x in arr:
        word = x.strip()
        if len(word) != 0:   # bỏ phần rỗng (do nhiều khoảng trắng)
            s2 += word + " "
    return s2.strip()        # bỏ khoảng trắng cuối cùng


# --- Kiểm thử ---
s = "   Trần   Duy   Thanh   "
print(s, "=>", len(s))
s = ToiUuChuoi(s)
print(s, "=>", len(s))
