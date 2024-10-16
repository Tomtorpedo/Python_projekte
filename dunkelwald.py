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
chars=[]
#   string=input()  das kann genutzt werden, um etwas einzugeben
string="^^<>>>v>v<<<^>v<<vv>>>>^^>^^>vv"
for i in string:
    chars.append(i) #wandelt einen string in eine liste mit einzelnen charaktern
vektoren_x=[]
vektoren_y=[]
pfad=chars
for i in pfad:                  #für jeden wert wird ein vektor erstellt
    if i=="^":
        vektoren_x.append(1)
        vektoren_y.append(0)
    elif i==">":
        vektoren_x.append(0)
        vektoren_y.append(1)
    elif i=="v":
        vektoren_x.append(-1)
        vektoren_y.append(0)
    elif i=="<":
        vektoren_x.append(0)
        vektoren_y.append(-1)

koordinaten_x=[0]               #das koordinatensystem wird aufgestellt
koordinaten_y=[0]
rx=0
ry=0
is_shortest_path=True
for i in vektoren_x:
    rx=rx+i
    koordinaten_x.append(rx)     # die vektoren werden eingepflegt >> es entsteht eine "karte"
for i in vektoren_y:
    ry=ry+i
    koordinaten_y.append(ry)

besuchte_koordinaten_x=[]
besuchte_koordinaten_y=[]
for i in range(len(chars)+1):
    if koordinaten_x.count(koordinaten_x[i])>1 and koordinaten_y.count(koordinaten_y[i])>1 and koordinaten_x[i] not in besuchte_koordinaten_x and koordinaten_y[i] not in besuchte_koordinaten_y:
        print("sie sind schonmal an den koordinaten", koordinaten_x[i],"|",koordinaten_y[i],"gewesen.")
        is_shortest_path=False
        besuchte_koordinaten_x=koordinaten_x[i]
        besuchte_koordinaten_y=koordinaten_y[i]
