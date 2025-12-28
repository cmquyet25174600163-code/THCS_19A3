import du_lieu.tu_dien as l 
import du_lieu.danh_sach as s

so = [9,8,3,1,3,7]
du_lieu = {
    "ten":"Vu",
    "tuoi":18
}
sap_xep = s.sap_xep_tang_dan(so)
lay = l.lay_gia_tri(du_lieu,"tuoi")

print("Sắp xếp theo dữ liệu tăng dàn là :",sap_xep)
print("Lấy dữ liệu từ từ khóa",lay)
