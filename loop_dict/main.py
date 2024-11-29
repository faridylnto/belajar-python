# looping dictionary

nama_dict = {
    1 :"Farid",
    2 : "Muhammad",
    3 : "Yulianto",
    4 : "Winny",
    5 : "Andarilla"
}

for nama in nama_dict:
    print(nama) # keluarnya adalah key

# operator untuk mengambil item / iterable

keys = nama_dict.keys()
print(keys)

for key in nama_dict.keys():
    print(nama_dict.get(key))

values = nama_dict.values()
print(values)

for value in nama_dict.values():
    print(value)

items = nama_dict.items()
print(items)

for item in nama_dict.items():
    print(item)

for kunci, nilai in nama_dict.items():
    print(f"key : {kunci}, nilai : {nilai}")