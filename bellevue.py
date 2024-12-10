def namen_normalisieren(namen):
    namen.strip()
    vornamen,nachnamen=namen.rsplit(" ",1)

namen_normalisieren("tom kai blabla")
