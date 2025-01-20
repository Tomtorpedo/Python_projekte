import time
import toolbox
import random
class liste:
    def __init__(self):
        self.werte=[]

    def liste(self,größe:int)->list:
        self.werte=[]
        for i in range(größe):
            self.werte.append(i)
        return self.werte

def suche_1(x,liste)->bool:
    for wort in liste:
        if wort==x:
            return True
    return False

def suche_2(x,liste)->bool:
    status=False
    for wort in liste:
        if wort==x:
            status=True
    return status


analyse1=[]
analyse2=[]
l1=liste()
for i in range(5000):
    zahl=random.randrange(0,10000)
    zeit1=toolbox.timer(suche_1,zahl,l1.liste(10000))
    zeit2=toolbox.timer(suche_2,zahl,l1.liste(10000))
    analyse1.append(zeit1)
    analyse2.append(zeit2)
durchschnitt=0
for i in analyse1:
    durchschnitt+=i
durchschnitt=durchschnitt/len(analyse1)

durchschnitt1=0
for i in analyse2:
    durchschnitt1+=i
durchschnitt1=durchschnitt1/len(analyse2)
print(durchschnitt,"|",durchschnitt1,"|",durchschnitt1/durchschnitt)



