#python3

from math import floor

monety = [5, 2, 1]

kwota = int(input("Wprowadź kwotę do rozmienienia: "))
for i in range(0, len(monety)):
    if kwota == 0:
        break
    if kwota >= monety[i]:
        lmonet = kwota/monety[i]  # lmonet float
        lmonet = floor(lmonet) #lmonet int
        kwota = kwota - (lmonet * monety[i])
        print(f"Wydano {lmonet} -> {monety[i]}")

