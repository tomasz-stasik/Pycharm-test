
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
print("a) Jeśli chcesz dododać wciśnij 1")
print("b) Jeśli chcesz odjąć wciśnij 2")
print("c) Jeśli chcesz pomnożyć wciśnij 3")
print("d) Jeśli chcesz podzielić wciśnij 4")
c = int(input())

print("Podaj pierwszą liczbę")
a = int(input())

print("Podaj drugą liczbę")
b = int(input())

if c == 1:
    calc.dodaj(a, b)

if c == 2:
    calc.odejmij(a, b)

if c == 3:
    calc.mnozenie(a, b)

if c == 4:
    calc.dzielenie(a, b)
