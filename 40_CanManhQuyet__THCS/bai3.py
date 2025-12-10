def kiem_tra_so_armstrong(n):
    tong = sum(int(ch)**3 for ch in str(n))
    return tong == n

# Gọi hàm
n = int(input("Nhập số cần kiểm tra: "))
print("Là số Armstrong?" , kiem_tra_so_armstrong(n))
