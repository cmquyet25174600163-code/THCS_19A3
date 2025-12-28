import sys
sys.path.append(r"C:/Users/Admin/Desktop/40_CanManhQuyet_THCS-thcs/thu_vien_chung")

from thu_vien_chung import xu_ly_so

so = int(input("Nhập số cần kiểm tra: "))

snt = xu_ly_so.so_nguyen_to(so)

if(snt):
    print(f"{so} là số nguyên tố!")
else:
    print(f"{so} không là số nguyên tố!")