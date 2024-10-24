zahl=496
zwischensumme=0
for i in range(1,int(zahl**(1/2))+1):
    if zahl%i==0:
        zwischensumme+=i
        l=zahl/i
        zwischensumme+=l
if zwischensumme==2*zahl:
    print("die",zahl,"ist volkommen")
