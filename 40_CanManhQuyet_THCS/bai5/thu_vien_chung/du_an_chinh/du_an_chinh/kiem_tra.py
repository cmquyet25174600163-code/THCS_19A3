import sys
import os

# Thêm đường dẫn của thư mục thu_vien_chung
thu_vien_path = os.path.abspath("../thu_vien_chung")
sys.path.append(thu_vien_path)

# Import module xu_ly_so
import bai5.thu_vien_chung.du_an_chinh.xu_ly_so as xu_ly_so

# Gọi hàm kiểm tra số nguyên tố
so = 29
if xu_ly_so.kiem_tra_so_nguyen_to(so):
    print(f"{so} là số nguyên tố")
else:
    print(f"{so} không phải số nguyên tố")