matrix = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
is_square = True
row_count = len(matrix)
for row in matrix:
    col_count = 0
    for _ in row: col_count += 1
    if col_count != row_count:
        is_square = False
        break

if not is_square:
    print("Không phải ma trận vuông")
else:
    is_unit = True
    for i in range(row_count):
        for j in range(row_count):
            if i == j:
                if matrix[i][j] != 1: is_unit = False
            else:
                if matrix[i][j] != 0: is_unit = False
    print("Ma trận đơn vị:" if is_unit else "Không phải ma trận đơn vị")