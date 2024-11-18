# width and multiline

# Data

data_nama = "Ucup Surucup"
data_umur = 17
data_tinggi = 150.1
data_nomor_sepatu = 44

# string standard
data_string = f"nama = {data_nama}, umur = {data_umur}, tinggi = {data_tinggi}, nomor sepatu = {data_nomor_sepatu}"
print("Data String".center(30,"="))
print(data_string)

# string multiline
data_string = f"nama = {data_nama}, \numur = {data_umur}, \ntinggi = {data_tinggi}, \nnomor sepatu = {data_nomor_sepatu}"
print("\n"+"Data String".center(30,"="))
print(data_string)

# string multiline (kutip triplets)

data_string = f"""
nama = {data_nama}
umur = {data_umur}
nomor sepatu = {data_nomor_sepatu}
"""
print("\n"+"Data String".center(30,"="))
print(data_string)

# mengatur lebar
data_nama= "Ucup"
data_string = f"""
nama    = {data_nama:>5}
umur    = {data_umur:>5}
tinggi  = {data_tinggi:>5}
sepatu  = {data_nomor_sepatu:>5}
"""
print("\n"+"Data String".center(30,"="))
print(data_string)