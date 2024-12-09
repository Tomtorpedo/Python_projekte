from random import *
import json
import os.path

rand=randint(1,100)
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
speicherdatei="wörterbuch.json"
if os.path.isfile(speicherdatei):
    f=open(speicherdatei,"r",encoding="utf-8")
    de_en=json.loads(f.read())

eingabe=input("wort:")
#for deutsch,englisch in de_en.items():
#    if englisch==eingabe:
#        print(f"{englisch}:{deutsch}")
#        quit()
if eingabe not in de_en and rand > 15:
    print("dieses wort existiert nicht. :(")
elif eingabe not in de_en and rand <= 15:
    print("Das Wort existiert nicht, du Idiot!")
else:
    print(f"{eingabe}:{de_en[eingabe]}")
change=input("wollen sie die übersetzung ändern/hinzufügen?[y/N]")
if change == "y":
    änderung=input("neue definition:")
    de_en[eingabe]=änderung

print(de_en)

wörterbuch_json=json.dumps(de_en)
#datei schreiben
f=open("wörterbuch.json","w")
f.write(wörterbuch_json)
f.close