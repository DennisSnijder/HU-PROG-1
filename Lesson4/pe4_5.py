def kwadraten_som(grondgetallen: list) -> int:
    totaal = 0
    for getal in grondgetallen:
        if getal > 0:
            totaal += (getal * getal)

    return totaal

print(kwadraten_som([4, 5, 3, -81]))
