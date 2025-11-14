nam = int(input("Nhập một năm (ví dụ: 2024): "))
la_nam_nhuan = (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0)
print(f"\n--- Kết quả kiểm tra ---")
if la_nam_nhuan:
    print(f"Năm {nam} là năm nhuận.")
else:
    print(f"Năm {nam} không phải là năm nhuận.")
