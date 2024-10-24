zahl=521
def is_prime():
    for i in range(2,int(zahl**(1/2))+1):
        if zahl%i==0:
            return False
    return True
print(is_prime())