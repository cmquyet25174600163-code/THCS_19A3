def la_so_hoan_hao(n):
    return sum(i for i in range(1, n) if n % i == 0) == n

def tinh_tong_so_hoan_hao(a, b):
    tong = 0
    for x in range(a, b + 1):
        if la_so_hoan_hao(x):
            tong += x
    return tong

# Gọi hàm
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
print("Tổng số hoàn hảo:", tinh_tong_so_hoan_hao(a, b))
