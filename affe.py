def funktion(liste):
    if len(liste) == 1:
        return liste[0]        #wenn die liste nur einen eintrag hat, dann wird nur der eintrag ausgegeben

    vor_stelle = 0
    nach_stelle = 0

    for stelle in range(len(liste)):             #stelle wird in der liste hochgezählt
        if liste [stelle] < liste[vor_stelle]:   #wenn die vor_stelle, die vorher auf null gesetzt wurde, größer ist, als stelle, die durch die liste iteriert, dann werden sie gleich gesetzt
            vor_stelle = stelle                     #veriable_1 wird immer auf den kleinsten wert gesetzt
        if liste [stelle] > liste[nach_stelle]:   #wenn die nach_stelle, die vorher auf nul gesetzt wurde, kleiner ist, als stelle, die durch die liste iteriert, dann werden sie gleich gesetzt
            nach_stelle = stelle                     #nach_stelle wird immer auf den größten werr gesetzt

    if vor_stelle > nach_stelle:         #wenn nach_stelle vor vor_stelle kommt, dann werden beide getauscht
        tauschvariable = nach_stelle
        nach_stelle = vor_stelle
        vor_stelle = tauschvariable

    quokka = liste[:vor_stelle] + liste[vor_stelle+1:nach_stelle] + liste[nach_stelle+1:]     #größter und kleinster wert werden aussortiert
    dachs = funktion(quokka) 
    return dachs
list=[4, 7, 2, 9, 5, 8, 3, 6]
funktion(list)