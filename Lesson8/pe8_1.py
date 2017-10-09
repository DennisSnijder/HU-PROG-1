brown: set = {
    'Boxtel',
    'Best',
    'Breukenlaan',
    "Eindhoven",
    "Helmond 't Hout",
    "Helmond",
    "Helmond Brouwhuis",
    "Deurne"
}

green: set = {
    'Boxtel',
    "Best",
    "Breukenlaan",
    "Eindhoven",
    "Geldrop",
    "Heeze",
    "Weert"
}

print(green.intersection(green))
print(brown.difference(green))
print(brown.union(green))
