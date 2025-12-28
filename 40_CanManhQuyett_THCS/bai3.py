ds_so = [2, 4, 5, 7, 9, 8]
with open("so_nguyen.txt", "w", encoding="utf-8") as f:
    for so in ds_so:
        f.write(str(so) + "\n")
print("Đã ghi danh sách số nguyên vào file.")