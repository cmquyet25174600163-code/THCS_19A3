s = input("Nhập chuỗi: ")
chu_cai = chu_so = dac_biet = 0
for char in s:
    if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
        chu_cai += 1
    elif '0' <= char <= '9':
        chu_so += 1
    else:
        dac_biet += 1
print(f"Chữ cái: {chu_cai}, Chữ số: {chu_so}, Đặc biệt: {dac_biet}")