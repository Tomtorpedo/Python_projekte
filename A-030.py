import random
random_zahlen=[100]
for i in range(100):
    random_zahlen[i]=random.random

summe=0
for i in random_zahlen:
    summe+=i
print(summe/100)