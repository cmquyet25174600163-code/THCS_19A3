lst = [1, 2, 2, 3, 4, 1, 5]
ket_qua = []
for x in lst:
    da_co = False
    for y in ket_qua:
        if x == y:
            da_co = True
            break
    if not da_co:
        ket_qua.append(x)
print("Danh sách sau khi lọc:", ket_qua)