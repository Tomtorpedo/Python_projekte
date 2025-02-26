def merge(a:list, b:list)->list:
    """
    Zwei sortierte listen werden sortiert vereinigt."""
    
    c=[]
    ia=0 
    ib=0 
    
    while ia < len(a) and ib < len(b):
        if ib<len(b) and a[ia]<b[ib]:   #wenn b noch nicht durch gelaufen ist und a kleiner als b ist wird a in c eingefügt
            c.append(a[ia])
            ia+=1
        else:                #sonst wenn b noch nicht durch gelaufen ist, b also größer als a ist, wird b in c eingefügt
            c.append(b[ib])
            ib+=1                       
    if ia<len(a):                   #wenn b durch gelaufen ist, werden die restlichen einträge von a in c eingefügt
        c.extend(a[ia:])            
    if ib<len(b):                   #wenn a durch gelaufen ist, werden die restlichen einträge von b in c eingefügt
        c.extend(b[ib:])
    return c


def merge_sort(liste:list)->list:
    """sortiert eine liste"""
    if len(liste)==1:
        return liste
    if len(liste)>1:
        liste_rechts=liste[(len(liste)//2):]
        liste_links=liste[:(len(liste)//2)]
        liste_rechts=merge_sort(liste_rechts)
        liste_links=merge_sort(liste_links)
        liste_neu=merge(liste_links,liste_rechts)
        return liste_neu


