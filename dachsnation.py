produkt_preise = [
  #Produktname                           , Preis in Euro
  ("Dachs Deluxe Streu (5kg)"            , 4.99),
  ("Dachs Deluxe Streu (2kg)"            , 2.99),
  ("Dachs Spielstation"                  , 114.99),
  ("Dachs Faltgehege"                    , 229.99),
  ("Dachs Krallenpflege"                 , 7.99),
  ("Dachs Kuschelkissen"                 , 17.99),
  ("Dachs Bett"                          , 54.49),
  ("Dachs Leckerli"                      , 0.15),
  ("Dachs Trockenfutter (250g)"          , 3.49),
  ("Dachs Nassfutter (175g)"             , 4.49),
  ("Dachs Gourmet Dose (75g)"            , 3.19),
  ("Dr. Detlefs Dachs Deo"               , 2.99),
  ("Dr. Detlefs Dachs Augentropfen"      , 4.99),
  ("Dr. Detlefs Dachs Nasenglanz"        , 3.79),
  ("Dr. Detlefs Dachs Atemspray"         , 3.19),
  ("Dr. Detlefs Dachs Haarschleifen-Set" , 4.49),
  ("Vielleicht! Dachs Aufzuchtfutter"    , 0.79),
  ("Vielleicht! Dachs Streu"             , 1.29),
  ("Vielleicht! Dachs Fellpflege"        , 5.49),
  ("Vielleicht! Dachs Vorlesebuch"       , 4.99)
]
index = 0
for i in produkt_preise:
    index += 1
    print(index,i)      #der index wird vor den Eintrag geschoben und gedruckt
# die engabe startet        
eingabe = True
warenkorb = []
gesamtpreis = 0
while eingabe==True:
    items = input("Eingabe:\nFüge Gegenstände zu deinem Warenkorb hinzu, indem du den index eingibst.\ndrücke \"q\" um die Eingabe zu beenden.\n")
    if items=="q":
        eingabe=False
        break
    anzahl = input("Bestimme die Anzahl der hinzuzufügenden Gegenstände:\n")
    warenkorb.append(produkt_preise[int(items)-1][0])
    gesamtpreis = gesamtpreis + (int(anzahl)*float(produkt_preise[int(items)-1][1]))
    print("In Ihrem Warenkorb sind folgende dinge:")
    for j in warenkorb:
        print(j)
    print("\nDer Gesamtpreis beträgt",gesamtpreis,"€.")
    gddfhzs=input()