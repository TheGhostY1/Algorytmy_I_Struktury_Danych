t = [1, 2, 3, 15, -5, 120, 13, -60, 0]

min_value = t[0]
for i in t:
    if min_value >= i:
        min_value = i
    else:
        print("tablica jest pusta")
print(f"najmniejsza liczba w tablicy to : {min_value}")
