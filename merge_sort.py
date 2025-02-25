a:list=[1,3,4,7,19]
b:list=[2,3,5,6]

def merge(a:list, b:list)->list:
    """
    Zwei sortierte listen werden sortiert vereinigt. \n
    Die Funktion geht a durch und schaut für jedes Element ob es kleiner als das aktuelle Element von b ist"""
    
    #variablen werden initialisiert
    c:list=[]
    ia=0 #iterator a
    ib=0 #iterator b
    
    while ia < len(a):
        if ib<len(b) and a[ia]<b[ib]:   #wenn b noch nicht durch ist und a kleiner als b ist wird a in c eingefügt
            c.append(a[ia])
            ia+=1
        elif ib<len(b):                #sonst wenn b noch nicht durch ist, b also größer als a ist, wird b in c eingefügt
            c.append(b[ib])
            ib+=1
        else:                        #wenn b durch ist, werden die restlichen einträge von a in c eingefügt
            c.append(a[ia])
            ia+=1
    return c


print(merge(a,b))