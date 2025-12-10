# --- 1. Định nghĩa hàm giải phương trình ---
def giai_phuong_trinh_bac_nhat(a, b):
    # Ép kiểu đầu vào thành số thực để xử lý chính xác hơn
    a = float(a)
    b = float(b)

    if a != 0:
        # Trường hợp có nghiệm duy nhất: x = -b/a
        x = -b / a
        print(f"Với a={a}, b={b}: Phương trình có nghiệm duy nhất: x = {x}")
    elif b != 0:
        # Trường hợp a = 0 và b != 0: Vô nghiệm
        print(f"Với a={a}, b={b}: Phương trình vô nghiệm.")
    else:
        # Trường hợp a = 0 và b = 0: Vô số nghiệm
        print(f"Với a={a}, b={b}: Phương trình có vô số nghiệm.")

# --- 2. Gọi hàm (Sử dụng hàm) để kiểm tra các trường hợp ---

print("--- Kiểm tra các trường hợp ---")
giai_phuong_trinh_bac_nhat(2, -4)   # a=2, b=-4 (Nghiệm x=2)
giai_phuong_trinh_bac_nhat(0, 5)    # a=0, b=5 (Vô nghiệm)
giai_phuong_trinh_bac_nhat(0, 0)    # a=0, b=0 (Vô số nghiệm)
giai_phuong_trinh_bac_nhat(1, 10)   # a=1, b=10 (Nghiệm x=-10)


