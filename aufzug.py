aufzeichnungen = [
    2, 3, -4, 5, 6, 5, 4, -6, 2, -1, -4, -2, -5, -4, -3, -1, -2, 1, -2, -4, -4,
    -3, -4, -3, 7, -2, -4, 3, 1, -2, 2, -8, 10, 1, -3, 3, -3, -1, -2, -5, 2, -2,
    -1, -2, -5, -9, 2, 5, 6, -4, -1, -2, -5, -3, -2, 6, -3, -1, -6, 5, -6, 1,
    -3, -3, -1, -3, 5, 5, 4, -5, -8, 6, 4, 5, -12, -6, 2, 4, -9, 10, -7, -4, 2,
    1, -1, -3, -2, 4, -3, 1, -1, 2, -3, -7, -3, -8, -1, 12, -2, -4, -13, -2, -8,
    -2, 12, -4, 7, -2, -8, 5, 1, 4, 1, -5, 7, -3, 4, -3, -4, 2, 4, -4, -1, 3,
    -9, 3, -1, 1, 2, 6, 2, -4, -5, -2, 9, 2, 6, -4, -2, -2, 6, 2, 7, 3, -1, 6,
    -2, 9, 3, 4, -5, 10, 1, -12, -7, -2, 2, -5, 1, 10, -1, -5, 2, 7, 11, -2, 9,
    -5, -3, -6, -6, -1, -4, -3, 3, 1, 9, -6, -7, 5, 5, 1, 9, 5, -2, 1, -2, -4,
    9, 1, -3, 8, 3, -6, -3, 3, -1, -10, 3, -2, 5, 4, -1, 3, 1, 2, -2, 9, 7, -1,
    -7, -2, 10, -6, -2, 12, -3, -2, -2, -7, -1, 3, 3, -4, 8, -1, 8, -2, -12, 6,
    -4, -2, -4, 3, 3, 2, -9, -2, 1, 4, -4, -2, -3, -1, -6, 1, 5, 2, 5, -2, 3,
    -1, 4, -6, 4, 8, -1, 7, -3, 1, -3, -2, 5, -2, -4, 3, 8, 1, 1, -9, 4, -1, 8,
    8, -6, 3, 2, 12, 8, 6, 6, 4, -7, 3, 8, 3, -3, -7, 7, -3, -4, 7, -8, 3, 5, 3,
    -4, -2, 1, -6, -8, -3, -6, 6, 1, 7, -8, -2, 4, 1, 7, -4, 3, 2, 7, -3, -7,
    -9, 5, 8, 2, 5, -2, -6, 2, 3, -4, 1, 1, 5, -5, 3, 2, -11, 4, 1, -3, 3, -7,
    -5, -7, 3, -1, -1, 3, 5, -2, 5, 4, -5, 5, 2, 5, 4, 2, 5, -4, -5, -1, 6, 8,
    -2, -5, -2, 7, -4, 8, -12, 6, -7, 1, -1, -3, 4, -1, 3, 1, 3, 5, 4, 4, 4, -2,
    6, -3, -10, 1, -9, 4, -10, 4, -3, 8, -3, 5, -4, -4, -4, -4, 5, -1, -3, -2,
    -2, 9, -1, -1, -4, -3, 10, 4, -3, -6, -2, -2, 3, 5, -6, 3, -1, 6, -1, -4,
    -9, -2, 4, 1, 5, -6, 2, 1, -3, 4, 6, -1, -2, 7, -3, -11, 2, -4, 3, -3, 4, 4,
    -1, -1, -3, 2, 6, -3, -1, -1, -1, -5, 5, 3, -3, 3, 3, -5, 1, -6, -13, 5, -2,
    4, -2, 1, -2, 6, 3, 2, -10, -3, -2, 10, 4, -11, 6, -5, -4, 2, -2, -2, 9, 1,
    2, 5, -1, 4, -8, 1, -5, 3, 1, 1, -10, -1, -2, -1, 1, 5, 4, -2, -1, 6, 2, -2,
    6, 1, 1, 4, -4, 2, -7, 4, -5, 3, -5, 4, -5, 2, -1, 1, -10, 3, -8, 8, 2, 8,
    -3, 6, 2, -3, -5, 10, -2, 2, 11, -3, 4, -2, 6, -7, 3, 10, 5, 13, 10, -2, -3,
    1, 9, -5, 6, -1, -10, -8, -5, -6, -1, -4, 5, 9, -1, 3, -8, 4, -6, 3, -6, -8,
    1, 4, 9, 2, -8, 10, -2, 11, -7, -9, -10, 4, -1, -7, -1, 3, -7, 2, -7, -5, 5,
    3, 2, 1, -1, 6, 6, -2, -5, -1, -5, -4, 1, 1, -1, 6, -2, -5, -2, 7, 8, -4,
    -1, -1, 1, -4, 2, -3, -3, 2, 2, 1, -2, -2
]
#print("Sie haben",len(aufzeichnungen),"Aufzeichnungen.")

"""
stockwerk = 0
for i in aufzeichnungen:
    stockwerk = stockwerk + i
print("Sie sind im ", stockwerk, ". Stockwerk.")
"""

"""
eine_tiefer = 0
for i in aufzeichnungen:
    if -1 == i:
        eine_tiefer += 1
print("Sie sind", eine_tiefer, "-mal eine Etage tiefer gefahren.")
"""
max_höhe = 0
stockwerk=0
for i in aufzeichnungen:
    stockwerk = stockwerk + i
    if i>0:
        stockwerk=max_höhe
        print(stockwerk)
