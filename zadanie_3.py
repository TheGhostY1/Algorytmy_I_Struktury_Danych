n = int(input("Podaj liczbe której szukasz w tablicy: "))
tablica = [1, 2, 3, -5, -25, 120, 525, 210, 0]

if n in tablica:
    print("Liczba znajduje sie w tablicy.")
else:
    print("Liczby nie ma w tablicy.")