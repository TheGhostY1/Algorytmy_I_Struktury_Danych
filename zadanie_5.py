t = [[9, 5, 42],[30, 20, 15]]
print("Tablica przed sortowaniem:",t)

for i in t:
    min_value = min(i)
    z = i.index(min_value)
    i[0], i[z] = i[z], i[0]

print("Tablica po sortowaniu od najmniejszej do najwiekszej:",t)
