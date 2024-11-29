data_0 = [1,2]
data_1 = [3,4]

data_2d = [data_0, data_1,10]
data_2d_copy = data_2d.copy()

print(f"data = {data_2d}")
print(f"data copy = {data_2d_copy}")

# mengambil data di nested list

data = data_2d[0]
print(f"data = {data}")

data = data_2d[0][1]
print(f"data = {data}")

# address
print(f"addres asli data 2d = {hex(id(data_2d))}")
print(f"addres copy data 2d = {hex(id(data_2d_copy))}")

print(f"address dari member ke -1")
print(f"addres asli data 2d = {hex(id(data_2d[0]))}")
print(f"addres copy data 2d = {hex(id(data_2d_copy[0]))}")

data_2d[1][0]= 5
data_2d[2] = 9
print(f"data = {data_2d}")  # list di dalam list tidak bisa dicopy (hanya mengcopy address / shallow copy)
print(f"data copy = {data_2d_copy}")

# kita gunakan deep copy

from copy import deepcopy
data_2d = [data_0, data_1,10]
data_2d_deepcopy = deepcopy(data_2d)
print(f"addres asli data 2d = {hex(id(data_2d))}")
print(f"addres copy data 2d = {hex(id(data_2d_deepcopy))}")


print(f"address dari member ke -1")
print(f"addres asli data 2d = {hex(id(data_2d[0]))}")
print(f"addres copy data 2d = {hex(id(data_2d_deepcopy[0]))}")

data_2d[1][0]= 30
print(f"data = {data_2d}") 
print(f"data copy = {data_2d_copy}")
print(f"data deep copy = {data_2d_deepcopy}")