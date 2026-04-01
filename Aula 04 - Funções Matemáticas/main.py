from turtle import *

def soma_10(x):
    return x + 10

t = Turtle()
t.speed(0)

# Plano cartesiano

# Eixo dos X
t.pu()
t.goto(-300, 0)
t.pd()
t.goto(300, 0)
t.stamp()

# Eixo dos Y
t.pu()
t.goto(0, -300)
t.pd()
t.goto(0, 300)
t.lt(90)
t.stamp()

t.color("red")
# t.pu()
# t.goto(-100, soma_10(-100))
# t.pd()
# t.goto(100, soma_10(100))

# O range vai do primeiro valor até o último -1
# print(list(range(-100, 100)))

# for x in range(-100, 100):
#     print(x)

t.color("blue")
t.pu()
t.goto(-200, soma_10(-200))
t.pd()
for x in range(-99, 101):
    t.goto(2 * x, soma_10(2*x))

mainloop()