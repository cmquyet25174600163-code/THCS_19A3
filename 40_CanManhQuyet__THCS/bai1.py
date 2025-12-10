def chuyen_doi_nhiet_do(do_c):
    return do_c * 9/5 + 32

# Gọi hàm (bắt buộc để có output)
do_c = float(input("Nhập độ C: "))
do_f = chuyen_doi_nhiet_do(do_c)
print("Độ F tương ứng là:", do_f)

