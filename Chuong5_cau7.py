#Câu 7: Tối ưu chuỗi danh từ
def ToiUuChuoiDanhTu(s):
    # Xóa khoảng trắng đầu và cuối, tách các từ
    arr = s.strip().split()
    
    # Ghép lại bằng 1 dấu cách, đồng thời viết hoa chữ cái đầu mỗi từ
    s2 = ' '.join(arr).title()
    
    return s2


# --- Chương trình chính ---
s = input("Nhập chuỗi danh từ: ")
print("Chuỗi gốc:", repr(s))
s = ToiUuChuoiDanhTu(s)
print("Chuỗi tối ưu:", s)
