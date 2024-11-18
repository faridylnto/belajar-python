# operasi komparasi

# setiap hasil operasi komparasi adalah boolean

a = 4
b = 2

# lebih besar dari >
print("==========Lebih besar dari==========")
hasil = a > 3
print(a,">",3,"=", hasil)
hasil = b > 3
print(b,">",3,"=", hasil)

# lebih kurang dari <
print("==========Lebih kurang dari==========")
hasil = a < 3
print(a,"<",3,"=", hasil)
hasil = b < 3
print(b,"<",3,"=", hasil)

# lebih besar dari sama dengan >=
print("==========Lebih besar dari sama dengan==========")
hasil = a >= 3
print(a,">=",3,"=", hasil)
hasil = b >= 3
print(b,">=",3,"=", hasil)
hasil = b >= 2
print(b,">=",2,"=", hasil)

# lebih besar dari sama dengan <=
print("==========Lebih kecil dari sama dengan==========")
hasil = a <= 3
print(a,"<=",3,"=", hasil)
hasil = b <= 3
print(b,"<=",3,"=", hasil)
hasil = b <= 2
print(b,"<=",2,"=", hasil)

# sama dengan ==
print("==========sama dengan==========")
hasil = a == 3
print(a,"==",3,"=", hasil)
hasil = b == 3
print(b,"==",3,"=", hasil)
hasil = b == 2
print(b,"==",2,"=", hasil)

# tidak sama dengan !=
print("==========tidak sama dengan==========")
hasil = a != 3
print(a,"!=",3,"=", hasil)
hasil = b != 3
print(b,"!=",3,"=", hasil)
hasil = b != 2
print(b,"!=",2,"=", hasil)

# is membandingkan memori / object identity
x = 5 # ini adalah assigment membuat object
y = 5
print("nilai x =",x,"id = ",hex(id(x)))
print("nilai y =",y,"id = ",hex(id(y)))
hasil = x is y
print("x is y =", hasil)

# is not membandingkan memori / object identity
x = 5 # ini adalah assigment membuat object
y = 5
print("nilai x =",x,"id = ",hex(id(x)))
print("nilai y =",y,"id = ",hex(id(y)))
hasil = x is not y
print("x is not y =", hasil)
