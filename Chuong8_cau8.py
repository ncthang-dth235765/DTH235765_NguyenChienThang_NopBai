#Câu 8: Thiết kế màn hình chuyển độ F thành độ C
from tkinter import *

def chuyenNhietDo():
    try:
        doF = float(stringDoF.get())
        doC = (doF - 32) * 5 / 9
        stringDoC.set(f"{doC:.2f} °C")
    except:
        stringDoC.set("Lỗi dữ liệu!")

root = Tk()
root.title("Chuyển độ F sang độ C")
root.configure(bg="yellow")
root.minsize(height=150, width=300)

# Khai báo biến chuỗi
stringDoF = StringVar()
stringDoC = StringVar()

# Giao diện
Label(root, text="Nhập độ F", bg="yellow", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10)
Entry(root, width=15, textvariable=stringDoF, fg="red", font=("Arial", 12)).grid(row=0, column=1, padx=5)

Button(root, text="Chuyển", command=chuyenNhietDo, bg="lightblue", font=("Arial", 10, "bold")).grid(row=1, column=1, pady=5)

Label(root, text="Độ C", bg="yellow", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=10)
Label(root, textvariable=stringDoC, bg="yellow", font=("Arial", 12, "bold")).grid(row=2, column=1, padx=10)

root.mainloop()
