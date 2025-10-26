#Câu 9: Phần mềm tính BMI
from tkinter import *

def tinhBMI():
    try:
        h = float(stringChieuCao.get())
        w = float(stringCanNang.get())
        bmi = w / (h * h)
        stringBMI.set(f"{bmi:.2f}")

        # Xác định tình trạng và nguy cơ
        if bmi < 18.5:
            tinhTrang = "Gầy"
            nguyCo = "Thấp"
        elif bmi < 25:
            tinhTrang = "Bình thường"
            nguyCo = "Trung bình"
        elif bmi < 30:
            tinhTrang = "Mập"
            nguyCo = "Hơi cao"
        else:
            tinhTrang = "Béo phì"
            nguyCo = "Rất cao"

        stringTinhTrang.set(tinhTrang)
        stringNguyCo.set(nguyCo)

    except:
        stringBMI.set("Lỗi dữ liệu!")
        stringTinhTrang.set("")
        stringNguyCo.set("")

root = Tk()
root.title("Tính chỉ số BMI")
root.configure(bg="yellow")
root.minsize(height=250, width=300)

# Khai báo biến
stringChieuCao = StringVar()
stringCanNang = StringVar()
stringBMI = StringVar()
stringTinhTrang = StringVar()
stringNguyCo = StringVar()

# Giao diện
Label(root, text="Nhập chiều cao:", bg="yellow", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=5, sticky=W)
Entry(root, textvariable=stringChieuCao, width=10, fg="red", font=("Arial", 12)).grid(row=0, column=1)

Label(root, text="Nhập cân nặng:", bg="yellow", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=5, sticky=W)
Entry(root, textvariable=stringCanNang, width=10, fg="red", font=("Arial", 12)).grid(row=1, column=1)

Button(root, text="Tính BMI", bg="lightblue", command=tinhBMI, font=("Arial", 12, "bold")).grid(row=2, column=1, pady=10)

Label(root, text="BMI của bạn:", bg="yellow", font=("Arial", 12)).grid(row=3, column=0, padx=10, pady=5, sticky=W)
Entry(root, textvariable=stringBMI, width=15, font=("Arial", 12)).grid(row=3, column=1)

Label(root, text="Tình trạng của bạn:", bg="yellow", font=("Arial", 12)).grid(row=4, column=0, padx=10, pady=5, sticky=W)
Entry(root, textvariable=stringTinhTrang, width=15, font=("Arial", 12)).grid(row=4, column=1)

Label(root, text="Nguy cơ phát triển bệnh:", bg="yellow", font=("Arial", 12)).grid(row=5, column=0, padx=10, pady=5, sticky=W)
Entry(root, textvariable=stringNguyCo, width=15, font=("Arial", 12)).grid(row=5, column=1)

Button(root, text="Thoát", command=root.quit, bg="lightblue", font=("Arial", 12)).grid(row=6, column=1, pady=10)

root.mainloop()
