# Zadanie 1
print("Zad. 1:")
punkty = int(input("Podaj liczbę zdobytych punktów: "))

if punkty > 80:
    print("Zaliczyłeś egzamin w terminie 0.")
elif punkty >= 50:
    print("Możesz poprawić swój wynik.")
else:
    print("Musisz poprawić egzamin.")
print()

# Zadanie 2
print("Zad. 2:")
x = float(input("Podaj x: "))
y = float(input("Podaj y: "))
z = float(input("Podaj z: "))

if x > y:
    x, y = y, x
if y > z:
    y, z = z, y
if x > y:
    x, y = y, x

print("Od najmniejszej do największej:", x, y, z)
print()

# Zadanie 3
print("Zad. 3:")
Nazwa_pliku = 'Raport_maj.xlsx'

if Nazwa_pliku.endswith('.xlsx'):
    print('Tak')
else:
    print('Nie')
print()

# Zadanie 5
plik = open('notwania_gieldowe.txt', 'w', encoding='utf-8')
plik.write("CDR, 120\nPKO, 55\nKGH, 140\n")
plik.close()
print("Zad. 5:")
print("a)")
plik = open('notwania_gieldowe.txt', 'r', encoding='utf-8')
for linia in plik:
    print(linia.strip())
plik.close()
print()

print("b)")
plik = open('notwania_gieldowe.txt', 'r', encoding='utf-8')
zawartosc = plik.read()
plik.close()

plik = open('notwania_gieldowe.txt', 'a', encoding='utf-8')
if not zawartosc.endswith('\n'):
    plik.write('\n')
plik.write('ALR, 113\n')
plik.close()

plik = open('notwania_gieldowe.txt', 'r', encoding='utf-8')
for linia in plik:
    print(linia.strip())
plik.close()
print()

# Zadanie 6
print("Zad. 6:")
litera = input("Wpisz jedną literę: ")

if litera.isupper():
    print("Duża litera")
elif litera.islower():
    print("Mała litera")
else:
    print("To nie jest litera")
print()

# Zadanie 7
print("Zad. 7:")
Hasło = 'pk47!jy0893'

if len(Hasło) == 11 and '!' in Hasło:
    print("Hasło jest poprawne")
else:
    print("Hasło jest nie poprawne")
print()

# Zadanie 8
print("Zad. 8:")
text = 'Studiuje-Informatykę'

print("Pierwsze trzy znaki:", text[:3])
print("Ostatnie dwa znaki:", text[-2:])