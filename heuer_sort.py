from toolbox import is_sorted

def heuer_sort(liste:list)->list:
    print(f"E{liste}")
    if is_sorted(liste):
        return liste
    maximum=liste.index(max(liste))
    if maximum==0:
        liste=liste[::-1]
        print(f"A{liste[:-1]}\n")
        liste_out=heuer_sort(liste[:-1])
        liste_out.append(liste[-1])
        return liste_out
    else:
        tausch=liste[:maximum+1]
        tausch=tausch[::-1]
        rest=liste[maximum+1:]
        tausch.extend(rest)
        liste=tausch
        print(f"A{liste}\n")
        liste=heuer_sort(liste)
        return liste


liste=[1,3,4,2,5,4]

print(f"Z{heuer_sort(liste)}")