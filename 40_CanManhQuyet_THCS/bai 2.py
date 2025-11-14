tong_so_keo = int(input("Nhập tổng số kẹo: "))
so_hoc_sinh = int(input("Nhập số học sinh: "))
if so_hoc_sinh == 0:
     print("Không thể chia kẹo cho 0 học sinh.")
else:
     keo_moi_hoc_sinh = tong_so_keo // so_hoc_sinh
     keo_con_thua = tong_so_keo % so_hoc_sinh
print(f"\n--- Kết quả chia kẹo ---")
print(f"Tổng số kẹo: {tong_so_keo}")
print(f"Số học sinh: {so_hoc_sinh}")
print(f"Mỗi học sinh nhận được: {keo_moi_hoc_sinh} viên kẹo.")
print(f"Số kẹo còn thừa: {keo_con_thua} viên.")