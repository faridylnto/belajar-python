# Import

# fungsinya adalah untuk mengambil program dari file external .py

# 1. Untuk menyambung program dari external dan menjalankannya
import program_print
import program_farid

# 2. Import dengan data
import variabel
import variabel_2
# data ada di namespace variable
print(variabel.data)
print(variabel_2.data)

# 3. Import dengan fungsi
import matematika
hasil = matematika.tambah(4,5)
print(hasil)