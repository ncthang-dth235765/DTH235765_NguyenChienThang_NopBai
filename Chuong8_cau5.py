#Câu 5: Màn hình đăng nhập
from tkinter import *
from tkinter import messagebox

def change_password():
    old_pw = entry_old.get()
    new_pw = entry_new.get()
    confirm_pw = entry_confirm.get()

    # Giả sử mật khẩu cũ là "1234"
    if old_pw != "1234":
        messagebox.showerror("Error", "Old password is incorrect!")
        return

    if new_pw == "":
        messagebox.showwarning("Warning", "New password cannot be empty!")
        return

    if new_pw != confirm_pw:
        messagebox.showerror("Error", "New passwords do not match!")
        return

    messagebox.showinfo("Success", "Password changed successfully!")
    root.destroy()

def cancel_action():
    root.destroy()

root = Tk()
root.title("Enter New Password")
root.geometry("350x180")
root.resizable(False, False)

# Tiêu đề
Label(root, text="Enter New Password", bg="#7A67EE", fg="white", font=("Arial", 10, "bold"),
      anchor=W, padx=10).pack(fill=X)

frame = Frame(root, pady=10)
frame.pack(padx=10)

# Các nhãn và ô nhập
Label(frame, text="Old Password:").grid(row=0, column=0, sticky=E, pady=3)
entry_old = Entry(frame, show="*", width=25)
entry_old.grid(row=0, column=1)

Label(frame, text="New Password:").grid(row=1, column=0, sticky=E, pady=3)
entry_new = Entry(frame, show="*", width=25)
entry_new.grid(row=1, column=1)

Label(frame, text="Enter New Password Again:").grid(row=2, column=0, sticky=E, pady=3)
entry_confirm = Entry(frame, show="*", width=25)
entry_confirm.grid(row=2, column=1)

# Nút OK / Cancel
button_frame = Frame(root)
button_frame.pack(pady=5)
Button(button_frame, text="OK", width=10, command=change_password).pack(side=LEFT, padx=5)
Button(button_frame, text="Cancel", width=10, command=cancel_action).pack(side=LEFT, padx=5)

root.mainloop()
