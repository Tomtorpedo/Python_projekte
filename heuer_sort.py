import toolbox as tbox

def heuer_sort(liste:list)->list:
    if tbox.is_sorted(liste):
        return liste
    maximum=liste.index(max(liste))
    if maximum==0:
        liste=liste[::-1]
        liste_out=heuer_sort(liste[:-1])
        liste_out.append(liste[-1])
        return liste_out
    else:
        tausch=liste[:maximum+1]
        tausch=tausch[::-1]
        rest=liste[maximum+1:]
        tausch.extend(rest)
        liste=tausch
        liste=heuer_sort(liste)
        return liste

liste=[1,3,2,5,4]


print(f"{heuer_sort(liste)}")