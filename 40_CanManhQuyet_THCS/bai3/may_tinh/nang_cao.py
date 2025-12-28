def luy_thua(co_so, so_mu):
    return co_so ** so_mu
def can_bac_hai(so):
     if so < 0:
         raise ValueError("Không thể lấy căn bậc hai của số âm.")
     return so ** 0.5