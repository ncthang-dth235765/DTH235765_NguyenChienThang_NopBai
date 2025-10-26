#Câu 3: Cộng trừ nhân chia
from tkinter import *

# =========================
# Các hàm xử lý
# =========================
def congAction():
    try:
        a = float(stringA.get())
        b = float(stringB.get())
        stringKQ.set(a + b)
    except ValueError:
        stringKQ.set("Lỗi nhập!")

def truAction():
    try:
        a = float(stringA.get())
        b = float(stringB.get())
        stringKQ.set(a - b)
    except ValueError:
        stringKQ.set("Lỗi nhập!")

def nhanAction():
    try:
        a = float(stringA.get())
        b = float(stringB.get())
        stringKQ.set(a * b)
    except ValueError:
        stringKQ.set("Lỗi nhập!")

def chiaAction():
    try:
        a = float(stringA.get())
        b = float(stringB.get())
        if b == 0:
            stringKQ.set("Không chia 0!")
        else:
            stringKQ.set(round(a / b, 2))
    except ValueError:
        stringKQ.set("Lỗi nhập!")

# =========================
# Giao diện chính
# =========================
root = Tk()
root.title("Máy tính 4 phép")
root.minsize(height=200, width=250)
root.resizable(False, False)

# Biến lưu dữ liệu
stringA = StringVar()
stringB = StringVar()
stringKQ = StringVar()

# Tiêu đề
Label(root, text="CỘNG - TRỪ - NHÂN - CHIA",
      fg="blue", font=("tahoma", 14, "bold")).grid(row=0, columnspan=3, pady=5)

# Khung chứa các nút
frameButton = Frame(root)
Button(frameButton, text="Cộng", command=congAction, width=10).pack(side=TOP, fill=X, padx=5, pady=2)
Button(frameButton, text="Trừ", command=truAction, width=10).pack(side=TOP, fill=X, padx=5, pady=2)
Button(frameButton, text="Nhân", command=nhanAction, width=10).pack(side=TOP, fill=X, padx=5, pady=2)
Button(frameButton, text="Chia", command=chiaAction, width=10).pack(side=TOP, fill=X, padx=5, pady=2)
frameButton.grid(row=1, column=0, rowspan=4, padx=10)

# Các ô nhập và hiển thị kết quả
Label(root, text="Số a:").grid(row=1, column=1)
Entry(root, width=15, textvariable=stringA).grid(row=1, column=2)

Label(root, text="Số b:").grid(row=2, column=1)
Entry(root, width=15, textvariable=stringB).grid(row=2, column=2)

Label(root, text="Kết quả:").grid(row=3, column=1)
Entry(root, width=15, textvariable=stringKQ, state="readonly").grid(row=3, column=2)

# Nút thoát
Button(root, text="Thoát", command=root.quit, width=10, bg="lightgray").grid(row=4, column=2, pady=5)

# Chạy chương trình
root.mainloop()
