# Yêu cầu người dùng nhập số kWh điện đã tiêu thụ
try:
    so_kwh = float(input("Nhập số kWh điện đã tiêu thụ: "))
except ValueError:
    print("Lỗi: Vui lòng nhập một số hợp lệ cho số kWh.")
    exit()
# Định nghĩa các mức giá
GIA_BAC_1 = 1678  # 0 - 100 kWh
GIA_BAC_2 = 1734  # 101 - 200 kWh
GIA_BAC_3 = 2014  # 201 - 300 kWh
# Khởi tạo tổng tiền
tong_tien = 0
if so_kwh < 0:
    print("Số kWh tiêu thụ không thể là số âm.")
elif so_kwh <= 100:
    # Trường hợp chỉ ở Bậc 1
    tong_tien = so_kwh * GIA_BAC_1
elif so_kwh <= 200:
    # Trường hợp đến Bậc 2
    # 1. Tính tiền cho 100 kWh đầu tiên (Bậc 1)
    tien_bac_1 = 100 * GIA_BAC_1
    # 2. Tính số kWh còn lại của Bậc 2
    kwh_bac_2 = so_kwh - 100
    tien_bac_2 = kwh_bac_2 * GIA_BAC_2
    # 3. Tính tổng tiền
    tong_tien = tien_bac_1 + tien_bac_2
elif so_kwh <= 300:
    # Trường hợp đến Bậc 3
    # 1. Tiền Bậc 1
    tien_bac_1 = 100 * GIA_BAC_1
    # 2. Tiền Bậc 2 (cho 100 kWh tiếp theo)
    tien_bac_2 = 100 * GIA_BAC_2
    # 3. Tính số kWh còn lại của Bậc 3
    kwh_bac_3 = so_kwh - 200
    tien_bac_3 = kwh_bac_3 * GIA_BAC_3
    # 4. Tính tổng tiền
    tong_tien = tien_bac_1 + tien_bac_2 + tien_bac_3
else:
    # Trường hợp tiêu thụ trên 300 kWh
    # Lưu ý: Theo đề bài chỉ có 3 bậc (0-300 kWh). 
    # Nếu thực tế có bậc 4 trở lên, bạn sẽ cần thêm logic ở đây.
    # Trong bài toán này, ta sẽ coi phần vượt 300 kWh vẫn tính theo giá Bậc 3
    # (hoặc bạn có thể chọn thông báo lỗi nếu không muốn tính tiếp).
    # *Giả sử* phần vượt 300 kWh vẫn áp dụng giá **Bậc 3**
    
    # 1. Tiền Bậc 1
    tien_bac_1 = 100 * GIA_BAC_1
    # 2. Tiền Bậc 2
    tien_bac_2 = 100 * GIA_BAC_2
    # 3. Tiền Bậc 3 (cho phần từ 201 trở đi)
    kwh_bac_3 = so_kwh - 200
    tien_bac_3 = kwh_bac_3 * GIA_BAC_3 
    
    tong_tien = tien_bac_1 + tien_bac_2 + tien_bac_3
# In ra kết quả
if so_kwh >= 0:
    # Định dạng tiền tệ cho dễ đọc (ví dụ: 100000 -> 100.000)
    # Tuy nhiên, chỉ in số nguyên cho tổng tiền
    print(f"\n--- THÔNG TIN HÓA ĐƠN ---")
    print(f"Số kWh tiêu thụ: **{so_kwh:,.2f} kWh**")
    print(f"Tổng số tiền điện phải trả: **{int(tong_tien):,} VNĐ**")