s = input("Nhập chuỗi: ")
n = int(input("Nhập n: "))
tu_hien_tai = ""
for char in s:
    if char != " ":
        tu_hien_tai += char
    else:
        do_dai = 0
        for _ in tu_hien_tai: do_dai += 1
        if do_dai > n:
            print(tu_hien_tai)
        tu_hien_tai = ""
# Kiểm tra từ cuối cùng
do_dai = 0
for _ in tu_hien_tai: do_dai += 1
if do_dai > n:
    print(tu_hien_tai)