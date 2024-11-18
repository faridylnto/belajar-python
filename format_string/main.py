# format string


# contoh generic
nama = "marlene"
format_str = f"hello {nama}"
print(format_str)

# boolean
boolean = True
format_str = f"boolean = {boolean}"
print(format_str)

# angka
angka = 2005.5
format_str = f"angka = {angka}"
print(format_str)

# bilangan bulat
angka = 15
format_str = f"bilangan bulat = {angka:d}"
print(format_str)

# bilangan dengan ordo ribuan
angka = 2000
format_str = f"ribuan = {angka:,}"
print(format_str)

# bilangan decimal
angka = 2005.54321
format_str = f"desimal = {angka:.2f}"
print(format_str)

# menampilkan leading zero
angka = 2005.54321
format_str = f"desimal = {angka:010.3f}"
print(format_str)

# menampilkan tanda + atau -
angka_minus = -10
angka_plus = 10.1234
format_minus = f"minus = {angka_minus:+d}"
format_plus = f"plus = {angka_plus:+.2f}"
print(format_minus)
print(format_plus)

# format persenan
persentase = 0.45
format_persen = f"persen = {persentase:.2%}"
print(format_persen)

# melakukan operasi aritmatika di dalam placehlder
harga = 10000
jumlah = 5
format_str = f"harga total = {harga * jumlah:,}"
print(format_str)

# format angka lain (binary, octal, hexadecimal)
angka = 255
format_binary = f"binar = {bin(angka)}"
format_octal = f"binar = {oct(angka)}"
format_hexa = f"binar = {hex(angka)}"
print(format_binary)
print(format_hexa)
print(format_octal)