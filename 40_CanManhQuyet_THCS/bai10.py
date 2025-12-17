matrix = [[1, 2, 3], [10, 11, 12], [4, 5, 6]]
max_tong = -float('inf')
hang_max = 0
for i in range(len(matrix)):
    tong_hang = 0
    for x in matrix[i]:
        tong_hang += x
    if tong_hang > max_tong:
        max_tong = tong_hang
        hang_max = i
print("Hàng có tổng lớn nhất là hàng số:", hang_max)