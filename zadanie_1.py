import math

a = int(input("Podaj liczbe a: "))

while a <= 0:
    print("Nie mozna podac liczby mniejszej lub rownej 0")
    a = int(input("Podaj liczbe a: "))


b = int(input("Podaj liczbe b: "))
c = int(input("Podaj liczbe c: "))
delta = math.pow(b, 2) - (4 * a * c)

if delta > 0:
    pierwiastek_delta = math.sqrt(delta)
    x1 = ( - b - pierwiastek_delta) / (2 * a)
    x2 = ( - b + pierwiastek_delta) / (2 * a)
    print(x1)
    print(x2)

elif delta == 0:
    x0 = (-b) / (2*a)
    print(x0)
else:
    print("Brak rozwiazania")
