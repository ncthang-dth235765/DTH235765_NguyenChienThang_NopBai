#Câu 5: Xử lý chuỗi với các hàm cơ bản
def dem_ky_tu(s):
    nguyen_am = "aeiouAEIOU"
    dem_hoa = 0
    dem_thuong = 0
    dem_so = 0
    dem_dac_biet = 0
    dem_trang = 0
    dem_nguyen_am = 0
    dem_phu_am = 0

    for ch in s:
        if ch.isupper():
            dem_hoa += 1
        elif ch.islower():
            dem_thuong += 1
        elif ch.isdigit():
            dem_so += 1
        elif ch.isspace():
            dem_trang += 1
        else:
            dem_dac_biet += 1

        # Đếm nguyên âm và phụ âm (chỉ xét chữ cái)
        if ch.isalpha():
            if ch in nguyen_am:
                dem_nguyen_am += 1
            else:
                dem_phu_am += 1

    print("Số chữ IN HOA:", dem_hoa)
    print("Số chữ in thường:", dem_thuong)
    print("Số chữ là chữ số:", dem_so)
    print("Số ký tự đặc biệt:", dem_dac_biet)
    print("Số ký tự khoảng trắng:", dem_trang)
    print("Số chữ nguyên âm:", dem_nguyen_am)
    print("Số chữ phụ âm:", dem_phu_am)


# --- Chương trình chính ---
s = input("Nhập vào một chuỗi: ")
dem_ky_tu(s)
