def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Gọi hàm
n = int(input("Nhập n: "))
print("Là số nguyên tố?", la_so_nguyen_to(n))

print("Các số nguyên tố trong khoảng 100 đến 500:")
for x in range(100, 501):
    if la_so_nguyen_to(x):
        print(x, end=" ")
