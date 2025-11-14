ten_dang_nhap = input("Nhập tên đăng nhập: ")
mat_khau = input("Nhập mật khẩu: ")
TEN_DANG_NHAP_DUNG = "admin"
MAT_KHAU_SAI_QUY_DINH = "password123"
duoc_cap_quyen = (ten_dang_nhap == TEN_DANG_NHAP_DUNG) and (mat_khau != MAT_KHAU_SAI_QUY_DINH)
print(f"\n--- Kết quả kiểm tra quyền ---")
if duoc_cap_quyen:
    print("Truy cập được cấp phép (Granted).")
else:
    print("Truy cập bị từ chối (Denied).")
