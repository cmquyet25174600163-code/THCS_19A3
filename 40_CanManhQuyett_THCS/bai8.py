import os

os.mkdir("temp_files")

with open("temp_files/file.txt", "w", encoding="utf-8") as f:
    f.write("khoa hoc du lieu")

os.rename("temp_files/file.txt", "temp_files/new_file.txt")

os.rename("temp_files/new_file.txt", "new_file.txt")

os.rmdir("temp_files")

print("ket qua")