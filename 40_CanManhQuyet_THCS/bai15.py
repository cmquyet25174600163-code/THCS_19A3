t = (1, 2, 3, 4, 5, 6)
chan = []
le = []
tong_chan = tong_le = 0
for x in t:
    if x % 2 == 0:
        chan.append(x)
        tong_chan += x
    else:
        le.append(x)
        tong_le += x
print(f"Tuple chẵn: {tuple(chan)}, Tổng: {tong_chan}")
print(f"Tuple lẻ: {tuple(le)}, Tổng: {tong_le}")