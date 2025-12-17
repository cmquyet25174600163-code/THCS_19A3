sv = {'An': 8, 'Bình': 7, 'Chi': 8, 'Dũng': 9}
nhom = {}
for ten, diem in sv.items():
    if diem not in nhom:
        nhom[diem] = [ten]
    else:
        nhom[diem].append(ten)
print(nhom)