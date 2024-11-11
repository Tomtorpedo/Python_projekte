def funktion(liste):
    if len(liste) == 1:
        return liste[0]        #wenn die liste nur einen eintrag hat, dann wird nur der eintrag ausgegeben

    stelle_1 = 0
    stelle_2 = 0

    for stelle_3 in range(len(liste)):            #stelle_3 wird in der liste hochgezählt
        if liste[stelle_3] < liste[stelle_1]:   #wenn die stelle_1, die vorher auf nul gesetzt wurde, größer ist, als stelle_3, die durch die liste iteriert, dann werden sie gleich gesetzt
            stelle_1 = stelle_3                     #veriable_1 wird immer auf den kleinsten wert gesetzt
        if liste[stelle_3] > liste[stelle_2]:   #wenn die stelle_2, die vorher auf nul gesetzt wurde, kleiner ist, als stelle_3, die durch die liste iteriert, dann werden sie gleich gesetzt
            stelle_2 = stelle_3                     #stelle_2 wird immer auf den größten werr gesetzt

    if stelle_1 > stelle_2:         #wenn stelle_2 vor stelle_1 kommt, dann werden beide getauscht
        variable_4 = stelle_2
        stelle_2 = stelle_1
        stelle_1 = variable_4

    quokka = liste[:stelle_1] + liste[stelle_1+1:stelle_2] + liste[stelle_2+1:]     #größter und kleinster wert werden aussortiert
    dachs = funktion(quokka) 
    return dachs
list=[4, 7, 2, 9, 5, 8, 3, 6]
funktion(list)