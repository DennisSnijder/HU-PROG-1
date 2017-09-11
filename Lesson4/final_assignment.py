def standaardprijs(afstandKM: float) -> float:
    return afstandKM * 0.80


def ritprijs(leeftijd: int, weekendrit: bool, afstandKM: float):
    prijs = standaardprijs(afstandKM)

    if leeftijd < 12 or leeftijd >= 65:
        if weekendrit:
            prijs = prijs * 0.65
        else:
            prijs = prijs * 0.70
    else:
        if weekendrit:
            prijs = prijs * 0.60
    return prijs
