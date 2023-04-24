a = int(input("Podaj a:"))
t = [1,2,10,-11]
i = 0

while i<4:
    if t[i] == a:
        print("Znajduje się")
        exit()
    else:
        i+= 1
print("Nie znajduje sie")