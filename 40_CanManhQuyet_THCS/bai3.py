s = input("Nhập chuỗi: ")
ket_qua = ""
tam = ""
# Loại bỏ khoảng trắng đầu/cuối và chuẩn hóa giữa
dang_co_khoang_trang = True
for char in s:
    if char != " ":
        ket_qua += char
        dang_co_khoang_trang = False
    elif not dang_co_khoang_trang:
        ket_qua += " "
        dang_co_khoang_trang = True
# Xóa khoảng trắng thừa ở cuối nếu có
s_final = ""
length = 0
for _ in ket_qua: length += 1
if length > 0 and ket_qua[length-1] == " ":
    for i in range(length - 1):
        s_final += ket_qua[i]
else:
    s_final = ket_qua
print(f"Chuỗi sau khi xử lý: '{s_final}'")