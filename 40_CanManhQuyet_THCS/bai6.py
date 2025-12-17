lst = [1, 2, 3, 4, 5, 6]
tong_chan = tong_le = 0
for x in lst:
    if x % 2 == 0:
        tong_chan += x
    else:
        tong_le += x
print(f"Tổng chẵn: {tong_chan}, Tổng lẻ: {tong_le}")