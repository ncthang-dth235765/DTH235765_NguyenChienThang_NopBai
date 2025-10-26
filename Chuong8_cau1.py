#Câu 1: Giải phương trình bậc 1

from tkinter import *

# -------------------------------
# Hàm xử lý các nút chức năng
# -------------------------------
def tiepAction():
    stringHSA.set("")
    stringHSB.set("")
    stringKQ.set("")

def giaiAction():
    try:
        a = float(stringHSA.get())
        b = float(stringHSB.get())

        if a == 0 and b == 0:
            stringKQ.set("Vô số nghiệm")
        elif a == 0 and b != 0:
            stringKQ.set("Vô nghiệm")
        else:
            x = -b / a
            stringKQ.set(f"x = {x:.2f}")
    except ValueError:
        stringKQ.set("Lỗi: Nhập hệ số không hợp lệ")

# -------------------------------
# Giao diện chính
# -------------------------------
root = Tk()
root.title("Giải phương trình bậc 1 - facebook.com/duythanhcse")
root.minsize(height=180, width=300)
root.resizable(height=True, width=True)

# Biến lưu dữ liệu
stringHSA = StringVar()
stringHSB = StringVar()
stringKQ = StringVar()

# -------------------------------
# Thành phần giao diện
# -------------------------------
Label(root, text="PHƯƠNG TRÌNH BẬC 1", fg="red", font=("Tahoma", 16), justify=CENTER).grid(row=0, columnspan=2, pady=5)

Label(root, text="Hệ số a:").grid(row=1, column=0, sticky=E)
Entry(root, width=25, textvariable=stringHSA).grid(row=1, column=1, padx=5, pady=2)

Label(root, text="Hệ số b:").grid(row=2, column=0, sticky=E)
Entry(root, width=25, textvariable=stringHSB).grid(row=2, column=1, padx=5, pady=2)

# Khung chứa các nút
frameButton = Frame(root)
Button(frameButton, text="Giải", width=8, command=giaiAction).pack(side=LEFT, padx=2)
Button(frameButton, text="Tiếp", width=8, command=tiepAction).pack(side=LEFT, padx=2)
Button(frameButton, text="Thoát", width=8, command=root.quit).pack(side=LEFT, padx=2)
frameButton.grid(row=3, columnspan=2, pady=5)

Label(root, text="Kết quả:").grid(row=4, column=0, sticky=E)
Entry(root, width=25, textvariable=stringKQ).grid(row=4, column=1, padx=5, pady=5)

# -------------------------------
# Chạy chương trình
# -------------------------------
root.mainloop()
