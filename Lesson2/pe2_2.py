cijferICOR = 10
cijferPROG = 10
cijferCSN = 10

gemiddelde = (cijferICOR + cijferPROG + cijferCSN) / 3
beloning = (cijferICOR + cijferPROG + cijferCSN) * 30
overzicht = 'Mijn cijfers (gemiddeld een ' + str(gemiddelde) + ') leveren een beloning van € ' + str(beloning) + ' op!'

print(overzicht)