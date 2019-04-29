class Calculator():

    def dodaj(self, a, b):
        wynik = a + b
        print("Twój wynik dodawania to {}".format(wynik))

    def odejmij(self, a, b):
        wynik = a - b
        print("Twój wynik odejmowania to {}".format(wynik))

    def mnozenie(self, a, b):
        wynik = a * b
        print("Twój wynik mnożenia to {}".format(wynik))

    def dzielenie(self, a, b):
        wynik = a / b
        print("Twój wynik dzielenia to {}".format(wynik))


calc = Calculator()

print("Podaj jakie chcesz wykonać działanie:")
print("Naciśnij 1 jeśli chcesz dododać ")
print("Naciśnij 2 jeśli chcesz odejmować")
print("Naciśnij 3 jeśli chcesz pomnożyc")
print("Naciśnij 4 jeśli chcesz podzielić")

c = int(input())

if c == 1 or c == 2 or c == 3 or c == 4:

    print("Podaj pierwszą liczbę")
    a = float(input())

    print("Podaj drugą liczbę")
    b = float(input())

    if c == 1:
        calc.dodaj(a, b)

    if c == 2:
        calc.odejmij(a, b)

    if c == 3:
        calc.mnozenie(a, b)

    if c == 4:
        calc.dzielenie(a, b)
else: print("Nie ma takiego działania. Program zatrzymany.")
print("Podaj jakie chcesz wykonać działanie:")
print("Naciśnij 1 jeśli chcesz dododać ")
print("Naciśnij 2 jeśli chcesz odejmować")
print("Naciśnij 3 jeśli chcesz pomnożyc")
print("Naciśnij 4 jeśli chcesz podzielić")

c = int(input())

if c == 1 or c == 2 or c == 3 or c == 4:

    print("Podaj pierwszą liczbę")
    a = float(input())

    print("Podaj drugą liczbę")
    b = float(input())

    if c == 1:
        calc.dodaj(a, b)

    if c == 2:
        calc.odejmij(a, b)

    if c == 3:
        calc.mnozenie(a, b)

    if c == 4:
        calc.dzielenie(a, b)