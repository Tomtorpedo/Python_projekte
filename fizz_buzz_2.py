def fizz_buzz(n):
    for i in range(1, n+1):
        r=0
        while i%3==0 and i%5<1:
            print("FIZZ! BUZZ!")
            r=1
            break
        while i%3==0 and r==0:
            print("FUZZ!")
            r=1
            break
        while i%5==0 and r==0:
            print("BUZZ!")
            r=1
            break
        while r==0:
            print(i)
            break
fizz_buzz(16)