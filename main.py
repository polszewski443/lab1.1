from math import *
# Zad1.
# Napisz pierwszy skrypt,
# w którym zadeklarujesz po dwie zmienne
# każdego typu a następnie wyświetl te zmienne
print('###########ZAD1############')
a = 2
b = 3
c = 2.5
d = 2.8
e = 'Pawel'
f = 'Olszewski'
print('Integers:', a, b)
print('Floats:', c, d)
print('Strings:', e, f)

# Zad2. Stwórz skrypt kalkulator,
# w którym wykorzystasz wszystkie podstawowe działania arytmetyczne
print('###########ZAD2############')
a = 2
b = 3
dodawanie = a + b
odejmowanie = a - b
mnozenie = a * b
dzielenie = ( a / b )
potega = pow(a, b)
logarytm = log(a, b)
pierwA = sqrt(a)
pierwB = sqrt(b)
print('Dzialania na a: ',a ,'oraz b: ', b)
print('Dodawanie: ', dodawanie)
print('Odejmowanie: ', odejmowanie)
print('Mnozenie: ', mnozenie)
print('Dzielenie: ', dzielenie)
print('Potegowanie: ', potega)
print('Logarytmowanie: ', logarytm)
print('Pierwiastek kwadratowy a oraz b: ', pierwA,'oraz', pierwB)

# Zad3. Napisz skrypt,
# w którym stworzysz operatory przyrostkowe
# dla operacji: +, -, *, /, **, %
print('###########ZAD3############')
print('Operatory przyrostkowe dla operacji: ')
a = 7
print('a =', a)
print('+ 10 =')
a += 10
print(a)
print('- 1 =')
a -= 1
print(a)
print('* 2 =')
a *= 2
print(a)
print('/ 2 =')
a /= 2
print(a)
print('** 5 =')
a **= 5
print(a)
print('% 2 =')
a %= 2
print(a)

# Zad4. Napisz skrypt, który policzy i wyświetli następujące wyrażenia:
print('###########ZAD4############')
print('a)')
print(exp(10))
print('b)')
print('Etapy:')
equ = sin(8)
print(equ)
equ1 = pow(equ,2)
print(equ1)
equ2 = equ1 + 5
print(equ2)
equ3 = log(equ2)
print(equ3)

def ntegostopniapierw(a,n):
    return pow(a,(1/n))
a = equ3
n = 6
equ4 = ntegostopniapierw(a,n)
print('Wynik:')
print(equ4)
print('c)')
print(floor(3.55))
print(ceil(4.80))

# Zad.5 Zapisz swoje imie i nazwisko w oddzielnych zmiennych wszystkie wielkimi literami.
# Użyj odpowiedniej metody by wyświetlić je pisane tak,
# że pierwsza litera jest wielka a poszostałe małe.
# (trzeba użyć metody capitalize)
print('###########ZAD5############')
imie = u'PAWEŁ'
nazwisko = u'OLSZEWSKI'
print(imie.capitalize() +' '+ nazwisko.capitalize())

# Zad.6 Napisz skrypt, gdzie w zmiennej string zapiszesz fragment tekstu
# piosenki z powtarzającymi się słowami np. „la la la”.
# Następnie użyj odpowiedniej funkcji, która zliczy występowanie
# słowa „la”. (trzeba użyć metody count)
print('###########ZAD6############')

piosenka = 'la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la'
slowo = 'la'
ile = piosenka.count(slowo)
print('Ilosc slow "la": ', ile)


# Zad.7 Do poszczególnych elementów łańcucha możemy się odwoływać przez podanie indeksu.
# Np. pierwszy znak zapisany w zmiennej imie uzyskamy przez imie[0].
# Zapisz dowolną zmienną łańcuchową i wyświetl jej drugą i ostatnią literę,
# wykorzystując indeksy.
print('###########ZAD7############')
imie = u'Paweł'
print('Druga litera: ', imie[1])
dlugosc = len(imie)
print('Ostatnia litera: ', imie[dlugosc-1])
print('Cale imie: ', imie)

# Zad.8 Zmienne łańcuchowe możemy dzielić wykorzystaj zmienną
# z Zad. 6 i spróbuj ją podzielić na poszczególne wyrazy.
# (trzeba użyć metody split)
print('###########ZAD8############')
podzial = piosenka.split()
print(podzial)

# Zad.9 Napisz skrypt, w którym zadeklarujesz zmienne typu:
# string, float i szestnastkowe.
# Następnie wyświetl je wykorzystując odpowiednie formatowanie.
print('###########ZAD9############')
zmienna1 = u'Paweł'
zmienna2 = u'Olszewski'
liczba1 = 6.3
liczba2 = 3.4
liczba3 = 5432
liczba4 = 1346
print('Zmienna1 to: %s, a zmienna 2 to: %s' % (zmienna1, zmienna2))
print('Liczba1 to: %f, a liczba2 to %f' % (liczba1, liczba2))
print('Liczba3(szesnastkowo) to: %#x, a liczba4(szesnastkowo) to %#x' % (liczba3, liczba4))




