#Câu 6: Trích lọc số âm trong chuỗi
import re

def NegativeNumberInStrings(s):
    # Tìm tất cả số có dấu trừ đứng trước
    nums = re.findall(r'-\d+', s)
    if nums:
        print("Các số nguyên âm trong chuỗi là:", ', '.join(nums))
    else:
        print("Không có số nguyên âm nào trong chuỗi.")

# --- Chương trình chính ---
chuoi = input("Nhập chuỗi: ")
NegativeNumberInStrings(chuoi)
