#Câu 4: Xử lý JSON File, Chuyển đổi String Json qua Python Object
import json

# Chuỗi JSON
jsonString = '{ "ma": "nv1", "age": 50, "ten": "Trần Duy Thanh" }'

# Chuyển JSON string thành đối tượng Python (dict)
dataObject = json.loads(jsonString)

# In ra toàn bộ đối tượng
print(dataObject)

# In từng thuộc tính
print("Mã =", dataObject["ma"])
print("Tên =", dataObject["ten"])
print("Tuổi =", dataObject["age"])
