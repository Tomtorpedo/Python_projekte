def is_prime(zahl):
    for i in range(2,int(zahl**(1/2))+1):
        if zahl%i==0:
            return False
    return True
for f in range(2,10000000000):
    print(f,"ist eine primzahl:", is_prime(f))