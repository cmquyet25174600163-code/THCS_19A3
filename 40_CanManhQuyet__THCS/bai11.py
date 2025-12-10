tich = lambda a, b, c: a * b * c

# Gọi hàm
a, b, c = map(float, input("Nhập 3 số: ").split())
print("Tích 3 số:", tich(a, b, c))
