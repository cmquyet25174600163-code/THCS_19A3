# Yêu cầu nhập lương cơ bản và số ngày công
try:
    luong_co_ban = float(input("Nhập mức lương cơ bản (VNĐ): "))
    so_ngay_cong = int(input("Nhập số ngày công trong tháng: "))
except ValueError:
    print("Lỗi: Vui lòng nhập số hợp lệ cho lương cơ bản và ngày công.")
    exit()
# Định nghĩa các hằng số
NGAY_CONG_CHUAN = 22
PHAN_TRAM_THUONG = 0.10  # 10%
PHAN_TRAM_PHAT = 0.05    # 5%
# 1. Tính lương một ngày
if luong_co_ban <= 0 or NGAY_CONG_CHUAN == 0:
    print("Lương cơ bản phải lớn hơn 0 và ngày công chuẩn phải là số dương.")
    exit()
    luong_mot_ngay = luong_co_ban / NGAY_CONG_CHUAN
# 2. Tính Tổng Lương thực tế (trước thưởng/phạt)
# Lương được tính dựa trên số ngày công thực tế nhân với lương một ngày
tong_luong_chua_thuong_phat = so_ngay_cong * luong_mot_ngay
# 3. Tính Thưởng hoặc Phạt
tien_thuong_phat = 0
loai_dieu_chinh = "Không"
if so_ngay_cong > NGAY_CONG_CHUAN:
    # Trường hợp Thưởng: số ngày công > 22
    tien_thuong_phat = tong_luong_chua_thuong_phat * PHAN_TRAM_THUONG
    loai_dieu_chinh = "Thưởng (+10%)"
elif so_ngay_cong < NGAY_CONG_CHUAN:
    # Trường hợp Phạt: số ngày công < 22
    tien_thuong_phat = tong_luong_chua_thuong_phat * -PHAN_TRAM_PHAT # Âm để dễ dàng tính tổng
    loai_dieu_chinh = "Phạt (-5%)"
# Nếu so_ngay_cong == 22, tien_thuong_phat vẫn là 0
# 4. Tính Lương thực nhận
luong_thuc_nhan = tong_luong_chua_thuong_phat + tien_thuong_phat
# In ra kết quả chi tiết
print(f"\n--- BẢNG LƯƠNG THÁNG ---")
print(f"Lương cơ bản: **{int(luong_co_ban):,} VNĐ**")
print(f"Số ngày công: **{so_ngay_cong} ngày**")
print("-" * 30)
print(f"Lương 1 ngày: **{luong_mot_ngay:,.0f} VNĐ**")
print(f"Tổng lương cơ sở: {int(tong_luong_chua_thuong_phat):,} VNĐ")
print(f"Điều chỉnh ({loai_dieu_chinh}): {int(abs(tien_thuong_phat)):,} VNĐ")
print("-" * 30)
print(f"**LƯƠNG THỰC NHẬN:** **{int(luong_thuc_nhan):,} VNĐ**")