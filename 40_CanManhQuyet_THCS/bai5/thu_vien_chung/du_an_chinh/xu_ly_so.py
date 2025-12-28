def kiem_tra_so_nguyen_to(so):
    for i in range(so):
        if so < 2:
            return False
    for i in range(2, so):
        if so % i == 0:
            return False
    return True