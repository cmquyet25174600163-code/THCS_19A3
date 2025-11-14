so_tien_goc = float(input("Nhập số tiền gửi ban đầu (VNĐ): "))
lai_suat_nam_phan_tram = float(input("Nhập lãi suất hàng năm (%): "))
lai_suat_nam = lai_suat_nam_phan_tram / 100
print(f"\n--- Kết quả tính lãi đơn ---")
print(f"Tiền gốc: {so_tien_goc:,.0f} VNĐ, Lãi suất/năm: {lai_suat_nam_phan_tram} %")
# --- Tính lãi sau 1 tháng ---
thoi_gian_thang = 1 / 12
lai_sau_1_thang = so_tien_goc * lai_suat_nam * thoi_gian_thang
print(f"Tiền lãi sau 1 tháng: {lai_sau_1_thang:,.2f} VNĐ")
# --- Tính lãi sau 2 quý ---
thoi_gian_quy = 2 * (3 / 12) # Hoặc 0.5
lai_sau_2_quy = so_tien_goc * lai_suat_nam * thoi_gian_quy
print(f"Tiền lãi sau 2 quý: {lai_sau_2_quy:,.2f} VNĐ")
# --- Tính lãi sau 3 năm ---
thoi_gian_nam = 3
lai_sau_3_nam = so_tien_goc * lai_suat_nam * thoi_gian_nam
print(f"Tiền lãi sau 3 năm: {lai_sau_3_nam:,.2f} VNĐ")