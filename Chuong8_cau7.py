#Câu 7: Thiết kế màn hình chuyển năm Dương Lịch thành Âm Lịch
from tkinter import *

# Danh sách Can và Chi
CAN = ["Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ", "Canh", "Tân", "Nhâm", "Quý"]
CHI = ["Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi", "Thân", "Dậu", "Tuất", "Hợi"]

def chuyenNam():
    try:
        nam = int(stringNamDuong.get())
        can = CAN[(nam + 6) % 10]
        chi = CHI[(nam + 8) % 12]
        stringNamAm.set(can + " " + chi)
    except:
        stringNamAm.set("Lỗi dữ liệu!")

# Giao diện chính
root = Tk()
root.title("Chuyển năm Dương lịch sang Âm lịch")
root.configure(bg="yellow")
root.minsize(height=150, width=300)

Label(root, text="Nhập năm dương:", bg="yellow", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10)
stringNamDuong = StringVar()
Entry(root, width=15, textvariable=stringNamDuong, fg="red", font=("Arial", 12)).grid(row=0, column=1, padx=5)

Button(root, text="Chuyển", command=chuyenNam, bg="lightblue", font=("Arial", 10, "bold")).grid(row=1, column=1, pady=5)

Label(root, text="Năm âm:", bg="yellow", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=10)
stringNamAm = StringVar()
Label(root, textvariable=stringNamAm, bg="yellow", font=("Arial", 12, "bold")).grid(row=2, column=1, padx=10)

root.mainloop()
