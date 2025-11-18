# Yêu cầu nhập số n từ người dùng
try:
    n = int(input("Nhập vào số nguyên dương n: "))
    if n <= 0:
        print("Vui lòng nhập một số nguyên dương.")
    else:
        # --- Tính S1 ---
        # S1 = 1 + 2 + 3 + 4 + ... + n
        S1 = sum(range(1, n + 1))
        # Hoặc dùng công thức cấp số cộng: S1 = n * (n + 1) // 2
        print(f"\n1. S1 = 1 + 2 + 3 + ... + n = **{S1}**")

        # --- Tính S2 ---
        # S2 = 1*2*3*4*...*n (tích của n số đầu tiên)
        S2 = 1
        for i in range(1, n + 1):
            S2 *= i
        print(f"2. S2 = 1*2*3*...*n (n!) = **{S2}**")

        # --- Tính S3 ---
        # S3 = 1 - 1/2 + 1/3 - 1/4 + ... + ((-1)**(n+1))/n
        # Đây là tổng chuỗi Leibniz cho ln(2)
        S3 = 0
        for i in range(1, n + 1):
            phan_tu = ((-1)**(i + 1)) / i
            S3 += phan_tu
        print(f"3. S3 = 1 - 1/2 + 1/3 - 1/4 + ... + ((-1)**(n+1))/n = **{S3:.6f}**") # Làm tròn 6 chữ số thập phân

        # --- Tính S4 ---
        # S4 = Tổng sigma(k=2 đến n) của 2/k
        # S4 = 2/2 + 2/3 + 2/4 + ... + 2/n
        S4 = 0
        for k in range(2, n + 1):
            phan_tu = 2 / k
            S4 += phan_tu
        print(f"4. S4 = Tổng(k=2 đến n) 2/k = **{S4:.6f}**") # Làm tròn 6 chữ số thập phân

except ValueError:
    print("⚠️ Lỗi: Vui lòng nhập một số nguyên dương hợp lệ.")