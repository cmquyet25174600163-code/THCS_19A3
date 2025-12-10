def tim_so_le_lon_nhat(a, b, c):
    le = [x for x in (a, b, c) if x % 2 == 1]
    return max(le) if le else -1

# Gọi hàm
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
print("Số lẻ lớn nhất:", tim_so_le_lon_nhat(a, b, c))
