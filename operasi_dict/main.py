# operator dictionary

data_dict = {
    "cup" : "ucup",
    "tong": "otong",
    "dung": "dudung"
}

# panjang dictionary
LENDICT = len(data_dict)
print(f"panjang dictionary : {LENDICT}")

# mengecek key exist atau tidak
KEY = "cup"
CHECKKEY = KEY in data_dict
print(f"apakah {KEY} ada di data_dict : {CHECKKEY}")

# mengakses value (read) menggunakan get
print(data_dict["cup"])
print(data_dict.get("cup"))
print(data_dict.get("kis","key tidak ditemukan"))

# Mengupdate data
data_dict["cup"] = "ganteng"
print(data_dict)
data_dict["sep"] = "asep"
print(data_dict)

data_dict.update({"cup": "ucup surucup"})
print(data_dict)
# jika memasukkan data menggunakan update yang tidak ada, maka akan langsung ditambahkan data baru 
data_dict.update({"far": "farid"})
print(data_dict)

# mendelet data dict
del data_dict["far"]
print(data_dict)