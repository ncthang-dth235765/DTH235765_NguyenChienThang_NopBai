#Câu 6: Màn hình cấu hình Style cho Button
from tkinter import *

root = Tk()
root.title("frame 2")

# Các kiểu style (relief) có sẵn trong Tkinter
styles = ["raised", "sunken", "flat", "ridge", "groove", "solid"]

# Tạo nhiều hàng với độ dày border khác nhau
for i in range(5):
    Label(root, text=f"borderwidth = {i}").grid(row=i, column=0, padx=10, pady=5)
    for j, style in enumerate(styles):
        Button(root, text=style, borderwidth=i, relief=style, width=8).grid(row=i, column=j+1, padx=5, pady=5)

root.mainloop()
