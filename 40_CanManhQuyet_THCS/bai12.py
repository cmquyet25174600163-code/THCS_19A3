A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
# Giả sử A là m x n, B là n x p
m, n, p = len(A), len(A[0]), len(B[0])
if len(B) != n:
    print("Không thể nhân")
else:
    C = [[0]*p for _ in range(m)]
    for i in range(m):
        for j in range(p):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    print("Kết quả:", C)