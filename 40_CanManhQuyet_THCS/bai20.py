d = {'A': 70, 'B': 40, 'C': 55, 'D': 10}
ket_qua = {}
for k, v in d.items():
    if v > 50:
        ket_qua[k] = v
print("Dictionary sau khi lọc:", ket_qua)