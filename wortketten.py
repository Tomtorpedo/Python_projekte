
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
    lösungen=[]
    for r in wortliste:
        wörter=wortliste
        neue_liste=[]
        neue_liste.append(r)
        wörter.pop(0)
        länge=len(wörter)
        while  len(wörter)>0 and len(wörter)<länge:
            länge=len(wörter)
            for i in wörter:
                if i[0]==neue_liste[len(neue_liste)-1][-1]:
                    neue_liste.append(i)
                    wörter.remove(i)
                    break
        print(neue_liste)
        lösungen.append(neue_liste)
    return lösungen

def kette_möglich(wortliste):
    for i in wortliste:
        i.anfang=wortliste.count(i[0])
def to_graph(wortliste):
    graph={}
    for i in wortliste:
        anfang=i[0]
        ende=i[-1]
        if anfang not in graph:
            graph[anfang]=[]
        if ende not in graph:
            graph[ende]=[]
        graph[anfang].append(ende)
        graph[ende].append(anfang)
    return graph
graph=to_graph(kette3)
print(graph)


