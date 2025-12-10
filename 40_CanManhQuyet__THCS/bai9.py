def tinh_tong_chu_so(n):
    if n < 10:
        return n
    return n % 10 + tinh_tong_chu_so(n // 10)

# Gọi hàm
n = int(input("Nhập n: "))
print("Tổng chữ số:", tinh_tong_chu_so(n))
