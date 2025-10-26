#Câu 13: Xử lý XML File - Viết phần mềm Quản Lý Thiết Bị
from xml.dom.minidom import parse
import xml.dom.minidom

# ------------------------------
# HÀM ĐỌC DANH SÁCH NHÓM THIẾT BỊ
# ------------------------------
def doc_nhom_thiet_bi(file_path):
    DOMTree = xml.dom.minidom.parse(file_path)
    collection = DOMTree.documentElement
    nhoms = collection.getElementsByTagName("nhom")

    ds_nhom = []
    for nhom in nhoms:
        ma = nhom.getElementsByTagName('ma')[0].childNodes[0].data
        ten = nhom.getElementsByTagName('ten')[0].childNodes[0].data
        ds_nhom.append({'ma': ma, 'ten': ten})
    return ds_nhom


# ------------------------------
# HÀM ĐỌC DANH SÁCH THIẾT BỊ
# ------------------------------
def doc_thiet_bi(file_path):
    DOMTree = xml.dom.minidom.parse(file_path)
    collection = DOMTree.documentElement
    thietbis = collection.getElementsByTagName("thietbi")

    ds_tb = []
    for tb in thietbis:
        manhom = tb.getAttribute("manhom")
        ma = tb.getElementsByTagName('ma')[0].childNodes[0].data
        ten = tb.getElementsByTagName('ten')[0].childNodes[0].data
        ds_tb.append({'ma': ma, 'ten': ten, 'manhom': manhom})
    return ds_tb


# ------------------------------
# HIỂN THỊ DANH SÁCH NHÓM
# ------------------------------
def hien_thi_ds_nhom(ds_nhom):
    print("\n📂 DANH SÁCH NHÓM THIẾT BỊ:")
    for nhom in ds_nhom:
        print(f"→ {nhom['ma']} - {nhom['ten']}")


# ------------------------------
# HIỂN THỊ TOÀN BỘ THIẾT BỊ
# ------------------------------
def hien_thi_ds_thiet_bi(ds_tb):
    print("\n🧰 DANH SÁCH THIẾT BỊ:")
    for tb in ds_tb:
        print(f"→ {tb['ma']} - {tb['ten']} (Nhóm: {tb['manhom']})")


# ------------------------------
# LỌC THIẾT BỊ THEO NHÓM
# ------------------------------
def loc_theo_nhom(ds_tb, manhom):
    return [tb for tb in ds_tb if tb['manhom'] == manhom]


# ------------------------------
# TÌM NHÓM CÓ NHIỀU THIẾT BỊ NHẤT
# ------------------------------
def nhom_nhieu_thiet_bi_nhat(ds_nhom, ds_tb):
    thong_ke = {}
    for tb in ds_tb:
        manhom = tb['manhom']
        thong_ke[manhom] = thong_ke.get(manhom, 0) + 1

    # Tìm nhóm có số lượng thiết bị cao nhất
    nhom_max = max(thong_ke, key=thong_ke.get)
    so_luong = thong_ke[nhom_max]

    # Lấy tên nhóm
    ten_nhom = next((n['ten'] for n in ds_nhom if n['ma'] == nhom_max), "Không rõ")

    print(f"\n🏆 Nhóm có nhiều thiết bị nhất: {ten_nhom} ({nhom_max}) với {so_luong} thiết bị.")


# ------------------------------
# CHƯƠNG TRÌNH CHÍNH
# ------------------------------
def main():
    ds_nhom = doc_nhom_thiet_bi("nhomthietbi.xml")
    ds_tb = doc_thiet_bi("ThietBi.xml")

    hien_thi_ds_nhom(ds_nhom)
    hien_thi_ds_thiet_bi(ds_tb)

    # Lọc theo nhóm
    manhom = input("\nNhập mã nhóm cần xem thiết bị (vd: n1, n2, n3): ")
    ds_loc = loc_theo_nhom(ds_tb, manhom)
    if ds_loc:
        print(f"\n📋 Các thiết bị thuộc nhóm {manhom}:")
        for tb in ds_loc:
            print(f"→ {tb['ma']} - {tb['ten']}")
    else:
        print("❌ Không tìm thấy thiết bị nào cho nhóm này.")

    # Nhóm có nhiều thiết bị nhất
    nhom_nhieu_thiet_bi_nhat(ds_nhom, ds_tb)


# ------------------------------
if __name__ == "__main__":
    main()
