import matplotlib.pyplot as plt

#   ^^<>>>v>v<<<^>v<<vv>>>>^^>^^>vv
#aufgabe 1-3
"""
chars=[]
#   string=input()  das kann genutzt werden, um etwas einzugeben
string="^^<>>>v>v<<<^>v<<vv>>>>^^>^^>vv"
for i in string:
    chars.append(i) #wandelt einen string in eine liste mit einzelnen charaktern

pfad=chars

rückpfad=[]
def rückweg_aus_wald(pfad):
    pfad.reverse()          #die .reverse methode für listen wird verwendet
    return pfad
rückpfad=rückweg_aus_wald(pfad)

output="".join(rückpfad)        # die liste wird zu einem string zurück geformt
print(output)
"""
#aufgabe 5
#wenn man die anweisungen als vektoren aufschreibt sieht man, dass man häufiger am selben punkt borbei kommt, man könnte also abkürzen

#aufgabe 6
string="v>v^>>vv^><>^v>"
#string=input()

  #das kann genutzt werden, um etwas einzugeben
def geht_schneller_zurück(string):
    chars=[]
    for i in string:
        chars.append(i) #wandelt einen string in eine liste mit einzelnen charaktern
    vektoren=[]
    pfad=chars
    for i in pfad:                  #für jeden wert wird ein vektor erstellt
        if i=="^":
            vektoren.append((0,1))
        elif i==">":
            vektoren.append((1,0))
        elif i=="v":
            vektoren.append((0,-1))
        elif i=="<":
            vektoren.append((-1,0))
    koordinaten=[(0,0)]
    kx = 0
    ky= 0
    for i in vektoren:
        kx += i[0]
        ky += i[1]
        koordinaten.append((kx,ky))

    
    #hier wird nun gezählt, wie oft und an welcher stelle eine koordinate auftaucht
    #alles was sich zwischen zwei koordinaten befindet, die zwei mal auftauchen, wird gelöscht, da es sich dann um einen umweg handelt
    r=0
    besuchte_koordinaten=[]
    for i in koordinaten:
        if i in besuchte_koordinaten:
            punkt_ab_doppelung=besuchte_koordinaten.index(i)
            del besuchte_koordinaten[(punkt_ab_doppelung+1):(r+1)]
        else:
            besuchte_koordinaten.append(i)
        r+=1
    print(besuchte_koordinaten)
    print(koordinaten)
    x, y = zip(*besuchte_koordinaten)
    plt.scatter(x,y)
    plt.plot(0,0, "ro")
    plt.plot(kx,ky, "go")
    plt.show()
    x, y = zip(*koordinaten)
    plt.scatter(x,y)
    plt.plot(0,0, "ro")
    plt.plot(kx,ky, "go")
    plt.show()
geht_schneller_zurück(string)


"""
    x, y = zip(*koordinaten)
    plt.scatter(x,y)
    plt.plot(0,0, "ro")
    plt.plot(kx,ky,"go")
    print(koordinaten)
    plt.show()
"""

        

       


"""
    for i in range(len(chars)+1):
        if koordinaten.count(koordinaten_x[i])>1 and koordinaten_y.count(koordinaten_y[i])>1:
            #print("sie sind schonmal an den koordinaten", koordinaten_x[i],"|",koordinaten_y[i],"gewesen.")
            is_shortest_path=False
    return(not is_shortest_path)
print(geht_schneller_zurück(string))
"""