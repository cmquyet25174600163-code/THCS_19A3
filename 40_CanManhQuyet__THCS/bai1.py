# --- Định nghĩa hàm ---
def chuyen_doi_nhiet_do(do_c):
    """
    Hàm nhận vào nhiệt độ C và trả về nhiệt độ F tương ứng.
    """
    # Công thức: F = C * 9/5 + 32
    do_f = (do_c * 9/5) + 32
    return do_f

# --- Gọi hàm và in kết quả ---

# 1. Gọi hàm với giá trị 25 độ C
ket_qua_1 = chuyen_doi_nhiet_do(25)
print(f"25 độ C = {ket_qua_1} độ F")

# 2. Gọi hàm với giá trị 100 độ C
ket_qua_2 = chuyen_doi_nhiet_do(100)
print(f"100 độ C = {ket_qua_2} độ F")

# 3. Gọi hàm với giá trị 0 độ C
ket_qua_3 = chuyen_doi_nhiet_do(0)
print(f"0 độ C = {ket_qua_3} độ F")

