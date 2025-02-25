import random
liste=[6,4,3,7,8,5,2,1]

sorted_list=sorted(liste)

def sort1(liste)->list:
    while True:
        prev=0
        r=0
        for i in liste:
            if prev>i:
                liste[r-1],liste[r]=liste[r],liste[r-1]
            prev=i
            r+=1
        if liste==sorted_list:
            return liste

def sort2(liste)->list:
    if liste[0]>liste[1]:
        liste[0],liste[1]=liste[1],liste[0]
    if len(liste)>2:
        r_liste=liste[:len(liste)//2]
        l_liste=liste[len(liste)//2:]
        sort2(r_liste)
        sort2(l_liste)
        liste=r_liste+l_liste
        return liste

def bogosort(liste):
    while True:
        random.shuffle(liste)
        if liste==sorted_list:
            return liste

print(sort2(liste))	
print(sort1(liste))
print(bogosort(liste))
