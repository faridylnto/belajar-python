#  Teknik menduplilkasi list

a = ["Ucup","Otong","Dudung"]
print(f"a = {a}")

b = a # pass by reference
print(f"b = {b}")

# kita akan merubah member dari a
a[1] = "Michael"
b.sort()
print(f"a = {a}")
print(f"b = {b}")

# address dari kedua list a dan b

print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")

# menduplikasi list dengan copy
print("membuat list c dengan a.copy()")
c = a.copy() # full duplikat

print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")
print(f"address c = {hex(id(c))}")

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print("merubah data pertama di list c")
c[0] = "Dadang"

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print("merubah data kedua di list a")
a[1] = "Otong"

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")