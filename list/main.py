# -------list--------

# List adalah kumpulan - kumpulan data

# kumpulan data number
data_angka = [1,5,2,3]
print(data_angka)

# kumpulan data string
data_str = ["farid","Eko","Riki"]
print(data_str)

# kumpulan data boolean
data_boolean = [True,False,True]

# kumpulan data campuran
data_campuran = [1, "gorengan", True]
print(data_campuran)

# cara alternatif membuat list
data_range = range(0,10,2) # (start, stop, step)
print(data_range)
data_list = list(data_range)
print(data_list)

# membuat list dengan for loop, 
data_list_pakai_for = [i**3 for i in range(0,10)]
print(data_list_pakai_for)

# membuat list menggunakan for pake if
list_pake_for_if = [i for i in range(0,10)if i !=5]
print(list_pake_for_if)

# membuat list menggunakan for pake if (ganjil)
list_pake_for_if = [i for i in range(0,10) if i%2 != 0]
print(list_pake_for_if)