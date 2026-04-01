from turtle import *
from random import randint

# Corrida de Tartarugas
t1 = Turtle()
t1.shape("turtle")
t2 = Turtle()
t2.shape("turtle")

t1.speed(1)
t1.pu()
t1.color("red")
t1.goto(-200, 100)

t2.speed(1)
t2.pu()
t2.color("blue")
t2.goto(-200, 130)

for num in range(30):
    t1.fd(randint(5, 10))
    t2.fd(randint(5, 10))

mainloop()