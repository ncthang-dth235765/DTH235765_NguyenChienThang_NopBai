#Câu 5: Xử lý JSON File, Chuyển đổi Python Object qua String Json
import json

# Tạo một đối tượng Python (dictionary)
pythonObject = {
    "ten": "Trần Duy Thanh",
    "tuoi": 50,
    "ma": "nv1"
}

# Chuyển đối tượng Python sang chuỗi JSON
jsonString = json.dumps(pythonObject, ensure_ascii=False)

# Kết quả là một chuỗi JSON
print(jsonString)
