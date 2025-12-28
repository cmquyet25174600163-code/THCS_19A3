with open("vanban.txt", "rb") as file_nguon, open("ban_sao.txt", "wb") as file_dich:
    while True:
        du_lieu = file_nguon.read(1024)
        if not du_lieu:
            break
        file_dich.write(du_lieu)

print("Đã sao chép file thành công.")