lst = [1, 2, 3, 4, 5]
k = int(input("Nhập k: "))
n = 0
for _ in lst: n += 1
k = k % n
ket_qua = [0] * n
for i in range(n):
    moi = (i + k) % n
    ket_qua[moi] = lst[i]
print("List sau khi dịch:", ket_qua)