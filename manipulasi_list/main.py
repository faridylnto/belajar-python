#  manipulasi list

data = ["farid","eko","yulianto"]

# cara memanggil data yang ada dalam list
print(f"data index pertama {data[0]}")
print(f"data index kedua {data[1]}")
print(f"data index ketiga {data[2]}")
print(f"data index terakhir {data[-1]}")

# mengambil info jumlah data dalam list
panjang_data = len(data)
print(f"Panjang data list adalah {panjang_data}")

# manipulasi data list
# menambahkan data pada list sesuai posisi
print(f"data sebelum di tambah {data}")
data.insert(1,"Jhonny")
print(f"data sesudah di tambah {data}")

# menanbahkan data di akhir list
data.append("Shulk")
print(f"data sesudah di tambah {data}")

# menambahkan list dengan list
data_baru = ["winny","andarilla"]
data.extend(data_baru)
print(f"data sesudah di gabung {data}")

#merubah data
data[2] = "sharla"
print(f"data sesudah di rubah {data}")

# meremove data

data.remove("farid") # huruf harus sesuai dengan besar kecil
print(f"data sesudah di remove {data}")

# meremove data paling belakang
data_akhir = data.pop()
print(f"data akhir {data}")

print(data_akhir)