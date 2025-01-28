from toolbox import timer
import matplotlib.pyplot as plt
import random

def O_plotter(versuche,funktion,farbe):
    laufzeiten=[timer(funktion,0)]
    werte=[0]
    for i in range(1,versuche):
        laufzeit=timer(funktion,i)
        if abs(laufzeit-laufzeiten[-1])<laufzeit*0.6:
            werte.append(i)
            laufzeiten.append(laufzeit)
    plt.plot(werte,laufzeiten,color=farbe)
    print(laufzeiten)

