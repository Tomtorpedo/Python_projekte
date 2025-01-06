def namen_normalisieren(name):
    name.strip()
    Dr_titel=""
    if " " not in name:
        return name
    vorname,nachname=name.rsplit(" ",1)
    if "Dr." in vorname:
        Dr_titel="Dr. "
        vorname=vorname.strip("Dr. ")       #wichtig! leerzeichen nach dem dr. nicht entfernen. sonst wird der vorname mit leerzeichen abgekürzt
        print(vorname)
    if ("-" not in vorname) and (" " not in vorname):
        vorname=vorname[0]+"."
    elif ("-" in vorname) and (" " in vorname):
        erstname,zweitname=vorname.rsplit("-",1)
        egal,zwischenname=vorname.rsplit(" ",1)
        vorname=erstname[0]+".-"+zweitname[0]+". "+zwischenname[0]
    elif "-" in vorname:
        erstname,zweitname=vorname.rsplit("-",1)
        vorname=erstname[0]+".-"+zweitname[0]+"."
    elif " " in vorname:
        erstname,zwischenname=vorname.rsplit(" ",1)
        vorname=erstname[0]+"."+zwischenname[0]+"."
    return(Dr_titel+vorname+" "+nachname)
print(namen_normalisieren("Dr. tom-kai lala vervoort"))


f=open("gaeste.txt","r",encoding="utf-8")
for line in f:
    line=line.strip()
    eingabe,ausgabe=line.split("|")
    if namen_normalisieren(eingabe) != ausgabe:
        print(line,"|",namen_normalisieren(eingabe))