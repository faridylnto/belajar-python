# # latihan logika dan komparasi

# # membuat gabungan area rentang dari angka

# #++++++++3----------10+++++++

# input_user = float(input('masukan angka yang bernilai\nkurang dari 3\natau\nlebih besar dari 10\n:'))

# # memeriksa angka kurang dari 3
# is_kurang_dari = (input_user < 3)
# print('kurang dari 3 :',is_kurang_dari)

# # memeriksa angka lebih dari 10
# is_lebih_dari = (input_user > 10)
# print('lebih dari 10 :',is_lebih_dari)

# is_correct = is_kurang_dari or is_lebih_dari
# print("angka yang ada masukkan :", is_correct)

# #------3+++++++++10-------
# # kasus irisan
# print('\n',20*'=','\n')
# input_user = float(input('masukan angka yang bernilai\nlebih dari 3\ndan\nkurang dari 10\n:'))
# is_lebih_dari = (input_user > 3)
# print('lebih dari 3 :',is_lebih_dari)

# is_kurang_dari = (input_user < 10)
# print('kurang dari 10 :',is_kurang_dari)
# is_correct = is_kurang_dari and is_lebih_dari
# print("angka yang ada masukkan :", is_correct)

input_user = float(input('masukan angka yang bernilai\nantara 0 sampai 5\ndan\nantara 8 sampai 11\n:'))
is_antara0_5 = (0 < input_user < 5)
print('antara 0 sampai 5 :',is_antara0_5)

is_antara8_11 = (8 < input_user < 11)
print('antara 8 sampai 11 :',is_antara8_11)
is_correct = is_antara0_5 and is_antara8_11
print("angka yang ada masukkan :", is_correct)

input_user = float(input('masukan angka yang bernilai\nkurang dari 0 atau lebih dari 5\ndan\nkurang dari 8 atau lebih dari 11\n:'))
is_antara0_5 = (input_user < 0 or input_user>5)
print('kurang dari 0 atau lebih dari 5 :',is_antara0_5)

is_antara8_11 = (5 < input_user < 8 or input_user > 11)
print('antara 5 sampai 8 atau lebih dari 11 :',is_antara8_11)
is_correct = is_antara0_5 or is_antara8_11
print("angka yang ada masukkan :", is_correct)