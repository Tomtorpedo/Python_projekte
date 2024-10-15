import turtle
alice = turtle.Turtle()
ecken=input("wie viele ecken?")
ecken=int(ecken)
i=ecken
# Bewegungen von Alice
while i > 0:
    alice.forward(500/ecken)
    alice.left(360/ecken)
    i=i-1

# Ende der Bewegungen Alice

turtle.done()