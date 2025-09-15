#Câu 7: Nhập vào một ngày (ngày, tháng, năm). Tìm ngày kế sau ngày vừa nhập (ngày/tháng/năm).
def la_nam_nhuan(nam):
    return (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0)

def ngay_ke_tiep(ngay, thang, nam):
    # Số ngày trong từng tháng
    ngay_thang = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Nếu năm nhuận thì tháng 2 có 29 ngày
    if la_nam_nhuan(nam):
        ngay_thang[1] = 29
    ngay += 1
    
    # Nếu ngày vượt quá số ngày trong tháng thì sang tháng mới
    if ngay > ngay_thang[thang - 1]:
        ngay = 1
        thang += 1
    
    # Nếu tháng vượt quá 12 thì sang năm mới
    if thang > 12:
        thang = 1
        nam += 1
    return ngay, thang, nam

# Nhập ngày, tháng, năm từ người dùng
ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))
ngay_tiep, thang_tiep, nam_tiep = ngay_ke_tiep(ngay, thang, nam)
print(f"Ngày kế tiếp là: {ngay_tiep}/{thang_tiep}/{nam_tiep}")