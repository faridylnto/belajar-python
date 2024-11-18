#operasi aritmatika

a = 10
b = 3

# operasi tambah
hasil = a + b
print(a,"+",b,"=",hasil)

# operasi pengurangan
hasil = a - b
print(a,"-",b,"=",hasil)

# operasi perkalian
hasil = a * b
print(a,"*",b,"=",hasil)

# operasi pembagian
hasil = a / b
print(a,"/",b,"=",hasil)

# operasi eksponen (pangkat)
hasil = a ** b
print(a,"**",b,"=",hasil)

# operasi modulus (sisa pembagian)
hasil = a % b
print(a,"%",b,"=",hasil)

# operasi floor division (kebalikan modulus)
hasil = a // b
print(a,"//",b,"=",hasil)

# prioritas operasi
'''
1. ()
2. Eksponen
3 perkalian dan teman -teman
4. pertambahan dan pengurangan
'''
x = 3
y = 2
z = 4

hasil = x**y*z+x/y-y%z//x
print(x,"**",y,"*",z,"+",x,"/",y,"-",y,"%",z,"//",x, "=", hasil)

# latihan konversi satuan temperatur

# program konersi celcius ke satuan lain

print("\nPROGRAM KONVERSI TEMPARTUR\n")
celcius = float(input("Masukan suhu dalam celcius = "))
print("suhu adalah", celcius, "celcius")

#reamur
reamur = (4/5)*celcius
print("suhu adalah", reamur, "reamur")

#fahrenheit
fahrenheit = (9/5)* celcius + 32
print("suhu adalah", fahrenheit, "fahrenheit")

#kelvin
kelvin = celcius + 273
print("suhu adalah", kelvin, "kelvin")

f = float(input("Masukan suhu dalam fahrenheit = "))
print("suhu adalah", f, "fahrenheit")

#kelvin
k = (5/9)*(f - 32) + 273
print("suhu dalam kelvin", k, "kelvin")

kl = float(input("Masukan suhu dalam kelvin = "))
print("suhu adalah", kl, "kelvin")

#fah
fh = (kl - 273)*(9/5)+32
print("suhu dalam kelvin", fh, "fahrenheit")