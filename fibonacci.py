from toolbox import timer
from O_plotter import O_plotter
import matplotlib.pyplot as plt

def fibonacci(n):
    if n>1:
        erg=fibonacci(n-1)+fibonacci(n-2)
        return erg
    else:
        return 1
    

def fibonacci2(n):
    erg=[1,1]
    for i in range(2,n+1):
        erg.append(erg[i-1]+erg[i-2])
    return erg[n]


zahlen=[3,5,7,10,15,20,42,100]


O_plotter(35,fibonacci,"blue")
O_plotter(35,fibonacci2,"red")
plt.show()

"""
for i in zahlen:
    print(i,":",(timer(fibonacci2,i)/1000),"ms")
"""