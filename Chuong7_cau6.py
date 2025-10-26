#Câu 6: Xử lý CSV File
import csv

# Mở file CSV và đọc dữ liệu
with open('datacsv.csv', newline='') as f:
    reader = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE)
    
    # Duyệt qua từng dòng và in ra 2 cột đầu
    for row in reader:
        print(row[0], "\t", row[1])
