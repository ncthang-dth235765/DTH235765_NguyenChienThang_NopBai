#Câu 8: Tách lấy tên bài hát
import os

def LayTenFile(path):
    """Lấy tên file có phần mở rộng"""
    return os.path.basename(path)

def LayTenFileKhongMoRong(path):
    """Lấy tên file không có phần mở rộng"""
    return os.path.splitext(os.path.basename(path))[0]


# --- Chương trình chính ---
duongdan = input("Nhập đường dẫn file nhạc: ")

print("Tên file có phần mở rộng:", LayTenFile(duongdan))
print("Tên file không có phần mở rộng:", LayTenFileKhongMoRong(duongdan))
