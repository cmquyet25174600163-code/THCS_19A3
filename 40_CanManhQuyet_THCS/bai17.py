d = {'a': 10, 'b': 50, 'c': 20}
max_val = -float('inf')
max_key = None
for k in d:
    if d[k] > max_val:
        max_val = d[k]
        max_key = k
print("Key có giá trị lớn nhất:", max_key)