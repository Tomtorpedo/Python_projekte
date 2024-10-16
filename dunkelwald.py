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

