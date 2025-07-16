import time
import random
import sys
import toolbox

sys.setrecursionlimit(10000)


class liste:
    def __init__(self):
        self.werte=[]

    def liste(self,größe:int)->list:
        self.werte=[]
        for i in range(größe):
            self.werte.append(i)
        return self.werte

class analyse:
    def __init__(self):
        self.analyse=[]
    def hinzufügen(self,zeit:int):
        self.analyse.append(zeit)
    def durchschnitt(self):
        durchschnitt=0
        for i in self.analyse:
            durchschnitt+=i
        return durchschnitt/len(self.analyse)
    def zahlen(self):
        return self.analyse

#####################################################################
#wurde durch toolbox.timer ersetzt 
'''
def timer(funktion,input1,input2)->int:
    start=time.perf_counter_ns()
    funktion(input1,input2)
    stop=time.perf_counter_ns()
    return(stop-start)
'''
#####################################################################

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

def suche_3(x,liste):
    if len(liste) == 0:
        return False
    elif liste[0] == x:
        return True
    else:
        return suche_3(x, liste[1:])

def suche_4(x,liste):
    if len(liste) == 0:
        return False
    elif liste[-1] == x:
        return True
    else:
        return suche_4(x, liste[:-1])

def suche_5(x,liste):
    if len(liste) == 0:
        return False
    elif liste[-1] == x:
        return True
    else:
        mid=len(liste)//2
        in_links = suche_5(x, liste[:mid])
        in_rechts = suche_5(x, liste[mid+1:])
        return in_links or in_rechts

#####################################################################

analyse1 = analyse()
analyse2 = analyse()
analyse3 = analyse()
analyse4 = analyse()
analyse5 = analyse()
l1=liste()

versuche=200
größe=5000
werte=[]

for i in range(versuche):
    zahl=random.randrange(0,größe)
    werte.append(zahl)
    zeit1=toolbox.timer(suche_1,zahl,l1.liste(größe))
    zeit2=toolbox.timer(suche_2,zahl,l1.liste(größe))
    zeit3=toolbox.timer(suche_3,zahl,l1.liste(größe))
    zeit4=toolbox.timer(suche_4,zahl,l1.liste(größe))
    zeit5=toolbox.timer(suche_5,zahl,l1.liste(größe))

    analyse1.hinzufügen(zeit1)
    analyse2.hinzufügen(zeit2)
    analyse3.hinzufügen(zeit3)
    analyse4.hinzufügen(zeit4)
    analyse5.hinzufügen(zeit5)

durchschnitt1=analyse1.durchschnitt()
durchschnitt2=analyse2.durchschnitt()
durchschnitt3=analyse3.durchschnitt()
durchschnitt4=analyse4.durchschnitt()
durchschnitt5=analyse5.durchschnitt()

print("Zeiten in µs:\n","iterativ ",durchschnitt1,"\n konstant ",durchschnitt1,"\n rekursiv von vorne ",durchschnitt3,"\n rekursiv von hinten",durchschnitt4,"\n rekursiv halbiert",durchschnitt5)
import matplotlib.pyplot as plt

plt.scatter(werte,analyse1.zahlen(),color="r")
plt.scatter(werte,analyse2.zahlen(),color="b")
plt.scatter(werte,analyse3.zahlen(),color="g")
plt.scatter(werte,analyse4.zahlen(),color="y")
plt.scatter(werte,analyse5.zahlen(),color="c")
plt.legend(["iterativ","konstant","rekursiv von vorne","rekursiv von hinten","rekursiv halbiert"])
plt.yscale("log")
plt.grid(True)
plt.xlabel("Algorithmen")
plt.ylabel("Zeit in µs")
plt.show()