#Câu 4: Phần mềm máy tính bỏ túi
from tkinter import *

# Hàm xử lý khi nhấn nút
def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(screen.get())
            screen.delete(0, END)
            screen.insert(END, result)
        except Exception as e:
            screen.delete(0, END)
            screen.insert(END, "Error")
    elif text == "Clr":
        screen.delete(0, END)
    else:
        screen.insert(END, text)

# Tạo cửa sổ chính
root = Tk()
root.title("Calculator")
root.geometry("250x300")
root.resizable(False, False)

# Ô hiển thị
screen = Entry(root, font=("Arial", 18), borderwidth=4, relief=SUNKEN, justify='right')
screen.pack(fill=X, ipadx=8, pady=5, padx=5)

# Khung chứa các nút
frame = Frame(root)
frame.pack()

# Các nút số và phép toán
buttons = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9'],
    ['+', '0', '-'],
    ['*', '/', '=', 'Clr']
]

# Tạo nút theo hàng
for row in buttons:
    row_frame = Frame(frame)
    row_frame.pack()
    for btn_text in row:
        button = Button(row_frame, text=btn_text, font=("Arial", 14), width=5, height=1)
        button.pack(side=LEFT, padx=2, pady=2)
        button.bind("<Button-1>", click)

root.mainloop()
