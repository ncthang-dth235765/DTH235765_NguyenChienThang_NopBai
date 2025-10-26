#Câu 11: Kiểm tra kết quả thực hiện
'''
Trường hợp 1:
def main():
 global val
 val = 5
 print(sum1(5))
 print(sum2())
 print(sum3())
main()
Trường hợp 2:
def main():
 global val
 val = 5
 print(sum1(5))
 print(sum3())
 print(sum2())
main()
Trường hợp 3:
def main():
 global val
 val = 5
 print(sum2())
 print(sum1(5))
 print(sum3())
main()


Trường hợp	Kết quả in ra
1	        5, 5, 0
2	        5, 5, 5
3	        5, 5, 0
'''