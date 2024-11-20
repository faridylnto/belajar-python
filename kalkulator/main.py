# kalkulator sederhana

print("Kalkulator".center(30,"="))

angka_1 = float(input("Masukkan angka pertama = "))
operator = input("Operator (+,-,*,/) : ")
angka_2 = float(input("Masukkan angka kedua = "))

if operator == "+" :
    hasil = angka_1 + angka_2
    print(f"Hasilnya adalah = {hasil}")
elif operator == "-":
    hasil = angka_1 - angka_2
    print(f"Hasilnya adalah = {hasil}")
elif operator == "*" or operator == "x":
    hasil = angka_1 * angka_2
    print(f"Hasilnya adalah = {hasil}")
elif operator == "/":
    hasil = angka_1 / angka_2
    print(f"Hasilnya adalah = {hasil}")
else:
    print("Operator salah")

print("Akhir dari program")