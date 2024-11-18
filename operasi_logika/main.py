# operasi logika

# not, or, and, xor

#NOT
print("==========NOT========")
a = True
c = not a
print('data a =', a)
print('-------NOT')
print('data c =',c)

# OR (jika salah satunya true maka hasilnya true)
print("==========OR========")
a = False
b = False
c = a or b
print(a,'OR',b,'=',c)
a = False
b = True
c = a or b
print(a,'OR',b,'=',c)
a = True
b = False
c = a or b
print(a,'OR',b,'=',c)
a = True
b = True
c = a or b
print(a,'OR',b,'=',c)

# and (jika salah satunya false maka hasilnya false)
print("==========AND========")
a = False
b = False
c = a and b
print(a,'and',b,'=',c)
a = False
b = True
c = a and b
print(a,'and',b,'=',c)
a = True
b = False
c = a and b
print(a,'and',b,'=',c)
a = True
b = True
c = a and b
print(a,'and',b,'=',c)

# XOR (akan true jika salah satu true)
print("==========XOR========")
a = False
b = False
c = a ^ b
print(a,'xor',b,'=',c)
a = False
b = True
c = a ^ b
print(a,'xor',b,'=',c)
a = True
b = False
c = a ^ b
print(a,'xor',b,'=',c)
a = True
b = True
c = a ^ b
print(a,'xor',b,'=',c)