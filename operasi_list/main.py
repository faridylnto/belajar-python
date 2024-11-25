data_angka = [1,5,1,4,1,3,5,6,7,2,3,5]

print(f"data angka = \n{data_angka}")

# count data

jumlah_data_4 = data_angka.count(4)
jumlah_data_3 = data_angka.count(3)
print(f"jumlah data 4 = {jumlah_data_4}")
print(f"jumlah data 3 = {jumlah_data_3}")

# ambil posisi data (index)
data = ["farid","yulianto","winny","andarilla"]
print(f"data = {data}")

index_data = data.index("yulianto")
print(f"index data yulianto = {index_data}")

# Mengurutkan data list
print(f"data sebelum di urutkan = {data_angka}")
data_angka.sort()
print(f"data setelah di urutkan = {data_angka}")

print(f"data sebelum di urutkan = {data}")
data.sort()
print(f"data setelah di urutkan = {data}")

# urutannya dibalik (reverse)
print(f"data sebelum di reverse = {data_angka}")
data_angka.reverse()
print(f"data setelah di reverse = {data_angka}")

print(f"data sebelum di reverse = {data}")
data.reverse()
print(f"data setelah di reverse = {data}")
