with open("san_pham.txt", "w", encoding="utf-8") as f:
    f.write("ID,Ten san pham,Gia\n")
    f.write("1,Laptop,1200\n")
    f.write("2,Chuot may tinh,25\n")
    f.write("3,Ban phim,75\n")
id_can_sua = input("Nhập ID sản phẩm cần cập nhật: ")
gia_moi = input("Nhập giá mới: ")
with open("san_pham.txt", "r", encoding="utf-8") as f:
    dong = f.readlines()
ds_moi = []
for d in dong:
    if d.startswith(id_can_sua + ","):
        phan = d.strip().split(",")
        phan[2] = gia_moi
        d = ",".join(phan) + "\n"
    ds_moi.append(d)
with open("san_pham.txt", "w", encoding="utf-8") as f:
    f.writelines(ds_moi)

print("Đã cập nhật giá sản phẩm.")