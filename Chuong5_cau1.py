#Câu 1: Kiểm tra chuỗi đối xứng
def CheckDoiXung(s):
    flag = True
    for i in range(len(s)):
        if s[i] != s[len(s) - i - 1]:
            flag = False
            break
    return flag


def main():
    print("Nhập 1 chuỗi:")
    s = input()
    if CheckDoiXung(s):
        print("Chuỗi bạn nhập đối xứng")
    else:
        print("Chuỗi bạn nhập không đối xứng")


# --- Chương trình chính ---
while True:
    main()
    print("Tiếp không Thím? (c/k):")
    s = input()
    if s.lower() == "k":
        break

print("CÁM ƠN THÍM")
