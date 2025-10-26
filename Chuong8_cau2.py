#Câu 2: Giải phương trình bậc 2
from tkinter import *
from math import sqrt

# -------------------------------
# Hàm xử lý
# -------------------------------
def giaiAction():
    try:
        a = float(stringHSA.get())
        b = float(stringHSB.get())
        c = float(stringHSC.get())

        # Trường hợp a = 0 => PT bậc 1: bx + c = 0
        if a == 0:
            if b == 0 and c == 0:
                stringKQ.set("Vô số nghiệm")
            elif b == 0 and c != 0:
                stringKQ.set("Vô nghiệm")
            else:
                x = -c / b
                stringKQ.set("x = " + str(round(x, 2)))
        else:
            delta = b ** 2 - 4 * a * c
            if delta < 0:
                stringKQ.set("Vô nghiệm")
            elif delta == 0:
                x = -b / (2 * a)
                stringKQ.set("Nghiệm kép x1 = x2 = " + str(round(x, 2)))
            else:
                x1 = (-b - sqrt(delta)) / (2 * a)
                x2 = (-b + sqrt(delta)) / (2 * a)
                stringKQ.set("x1 = " + str(round(x1, 2)) + "; x2 = " + str(round(x2, 2)))
    except ValueError:
        stringKQ.set("Lỗi: Nhập sai hệ số!")

def tiepAction():
    stringHSA.set("")
    stringHSB.set("")
    stringHSC.set("")
    stringKQ.set("")

# -------------------------------
# Giao diện
# -------------------------------
root = Tk()
root.title("Giải Phương Trình Bậc 2")
root.minsize(height=200, width=300)
root.resizable(False, False)

# Biến lưu dữ liệu
stringHSA = StringVar()
stringHSB = StringVar()
stringHSC = StringVar()
stringKQ = StringVar()

# Tiêu đề
Label(root, text="PHƯƠNG TRÌNH BẬC 2", fg="red", font=("Tahoma", 16)).grid(row=0, column=0, columnspan=2, pady=10)

# Nhập hệ số
Label(root, text="Hệ số a:").grid(row=1, column=0, sticky=E)
Entry(root, width=30, textvariable=stringHSA).grid(row=1, column=1, padx=5, pady=2)

Label(root, text="Hệ số b:").grid(row=2, column=0, sticky=E)
Entry(root, width=30, textvariable=stringHSB).grid(row=2, column=1, padx=5, pady=2)

Label(root, text="Hệ số c:").grid(row=3, column=0, sticky=E)
Entry(root, width=30, textvariable=stringHSC).grid(row=3, column=1, padx=5, pady=2)

# Các nút chức năng
frameButton = Frame(root)
Button(frameButton, text="Giải", width=8, command=giaiAction).pack(side=LEFT, padx=2)
Button(frameButton, text="Tiếp", width=8, command=tiepAction).pack(side=LEFT, padx=2)
Button(frameButton, text="Thoát", width=8, command=root.quit).pack(side=LEFT, padx=2)
frameButton.grid(row=4, columnspan=2, pady=5)

# Kết quả
Label(root, text="Kết quả:").grid(row=5, column=0, sticky=E)
Entry(root, width=30, textvariable=stringKQ).grid(row=5, column=1, padx=5, pady=5)

# -------------------------------
# Chạy chương trình
# -------------------------------
root.mainloop()
