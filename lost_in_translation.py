import json
import os.path

def idiot_am_werk(wort):
    matching=0
    best_match=""
    #vorschläge machen:
    for i in de_en:
        running=0
        for char in wort:
            running+=i.count(char)
        if running>matching:
            matching=running
            best_match=i         
    print(f"{wort} konnte nicht gefunden werden.\nmeinten sie:  {best_match} [Y/n]")
    fehler_einsehen=input()
    if fehler_einsehen.lower()=="n":
        neu=input("möchten sie ein neues Wort hinzufügen?[Y/n]")
        if neu.lower()=="n":
            print("taj pech gehabt...")
            quit()
        else:
            übersetzung=input(f"übersetzung für {wort}:")
            de_en[wort]=übersetzung
            neues_wort=True
            return wort
    else:
        return best_match



de_en ={"tisch":"table",
        "tasse":"mug",
        "flasche":"bottle",
        "fenster":"window",
        "stift":"pencil",
        "deine":"your",
        "mutter":"mother",
        "tee":"tea",
        "diese":"these",
        "nüsse":"nuts"}
#datei lesen, falls existiert
speicherdatei="woerterbuch.json"
if os.path.isfile(speicherdatei):
    f=open(speicherdatei,"r",encoding="utf-8")
    de_en=json.loads(f.read())
    f.close
neues_wort=False
eingabe=input("wort:")
for deutsch,englisch in de_en.items():
    if englisch==eingabe:
        print(f"Sie haben ein englisches wort eingegeben.\ndie Übersetzung lautet:{englisch}:{deutsch}")
        quit()


#wenn nicht existiert:
if eingabe not in de_en:
    eingabe=idiot_am_werk(eingabe)
print(f"{eingabe}:{de_en[eingabe]}")
change=input("wollen sie die übersetzung ändern/hinzufügen?[y/N]")
if change.lower() == "y":
    änderung=input("neue übersetzung:")
    de_en[eingabe]=änderung


wörterbuch_json=json.dumps(de_en)
#datei schreiben
f=open("wörterbuch.json","w")
f.write(wörterbuch_json)
f.close