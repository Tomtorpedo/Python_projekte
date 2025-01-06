
kette1=["sofa","alpenverein","nougat","terrier","regentonne","einkaufswagen","nadel","loeffel","lamahof","trampolin","nadel","lampe"]
kette2=["auflauf", "dampfzug", "eimer", "ente", "feld", "gehstock", "heuhaufen", "klavier", "nutria", "reh"]
kette3=["eisig", "graben", "laus", "leim", "leiter", "maultiere", "mittag", "norm", "normal", "sturm"]
def teste_kette(wortliste):
    ende=wortliste[0][0]
    for i in wortliste:
        anfang=i[0]
        print(anfang)
        if anfang is not ende:
            print("Das wort",i,"unterbricht die Kette.")
            return False
        ende=i[-1]
    return True

def mache_kette(wortliste):
    neue_liste=[]
    neue_liste.append(wortliste[0])
    wortliste.pop(0)
    while  len(wortliste)>0:
        länge=len(wortliste)
        for i in wortliste:
            if i[0]==neue_liste[len(neue_liste)-1][-1]:
                neue_liste.append(i)
                wortliste.remove(i)
                break
        if len(wortliste)==länge:
            return neue_liste
    return neue_liste

print(mache_kette(kette3))

