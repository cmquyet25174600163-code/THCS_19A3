lst = [1, 5, 7, -1, 5]
target = 6
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] + lst[j] == target:
            print(f"Cặp số: ({lst[i]}, {lst[j]})")