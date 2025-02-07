from toolbox import timer
import matplotlib.pyplot as plt
import random

def O_plotter(versuche,funktion,farbe):
    laufzeiten=[timer(funktion,0)]
    werte=[0]
    for i in range(1,versuche):
        laufzeit=timer(funktion,i)
        werte.append(i)
        laufzeiten.append(laufzeit)
    plt.scatter(werte,laufzeiten,color=farbe)
    print(laufzeiten)

