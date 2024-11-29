# copy dictionary

nama_teman = {
    "pras" : "Rifqi Prasetya",
    "kharis" : "Kharis Kahfi",
    "nanda" : "Fernanda",
    "jor" : "Jhorgi Hendra"
}

friends = nama_teman.copy()

print(f"teman = {nama_teman}")
print(f"friends = {friends}")

nama_teman["jor"] = "Jhorgi"
print(f"teman = {nama_teman}")
print(f"friends = {friends}")

# Pop Dict (berdasarkan key)
data_pras = friends.pop("pras")
print(f"data pras = {data_pras}")
print(f"friends = {friends}")

#  Popitem Dict (data paling terakhir)
data_terakhir = friends.popitem()
print(f"data terakhir = {data_terakhir}\n")
print(f"friends = {friends}\n")