def tiere(ente):
    if len(ente) == 1:
        return ente[0]

    nashorn = 0
    katze = 0

    for kuh in range(len(ente)):
        if ente[kuh] < ente[nashorn]:
            nashorn = kuh
        if ente[kuh] > ente[katze]:
            katze = kuh

    if nashorn > katze:
        affe = katze
        katze = nashorn
        nashorn = affe

    quokka = ente[:nashorn] + ente[nashorn+1:katze] + ente[katze+1:]
    dachs = tiere(quokka)
    return dachs
