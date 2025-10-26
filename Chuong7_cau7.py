#Câu 7: Xử lý lưu Excel File
import xlsxwriter

# Tạo file Excel và thêm 1 sheet
workbook = xlsxwriter.Workbook('demo.xlsx')
worksheet = workbook.add_worksheet()

# Thiết lập độ rộng các cột
worksheet.set_column('A:A', 5)
worksheet.set_column('B:B', 15)
worksheet.set_column('C:C', 20)
worksheet.set_column('D:D', 15)
worksheet.set_column('E:E', 15)

# Định dạng tiêu đề in đậm
bold = workbook.add_format({'bold': True})

# Ghi tiêu đề cột
worksheet.write('A1', 'STT', bold)
worksheet.write('B1', 'MÃ SẢN PHẨM', bold)
worksheet.write('C1', 'TÊN SẢN PHẨM', bold)
worksheet.write('D1', 'SỐ LƯỢNG', bold)
worksheet.write('E1', 'ĐƠN GIÁ', bold)

# Ghi dòng dữ liệu 1
worksheet.write('A2', 1)
worksheet.write('B2', 'SP1')
worksheet.write('C2', 'Coca')
worksheet.write('D2', 15)
worksheet.write('E2', 15000)

# Ghi dòng dữ liệu 2
worksheet.write('A3', 2)
worksheet.write('B3', 'SP2')
worksheet.write('C3', 'Pepsi')
worksheet.write('D3', 20)
worksheet.write('E3', 18000)

# Chèn logo vào file Excel (đường dẫn phải đúng)
worksheet.insert_image('B5', 'logo_UEL.png')

# Đóng file để lưu lại
workbook.close()
