from turtle import *

t = Turtle()
# Versão sem repetição
'''
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
'''

# Versão com repetição
t.color("red")
t.fillcolor("yellow")
t.begin_fill()
for num in range(4):
    # print(num)
    t.forward(50)
    t.left(90)
t.end_fill()

t.pu()
t.goto(100,100)
t.pd()

color = textinput("Escolha da cor", "Digite a cor desejada:")

t.color(color)
for num in range(3):
    # print(num)
    t.forward(80)
    t.left(120)

# 2o quadrante
t.pu()
t.goto(-30,150)
t.color("#e813c1")
t.stamp()
t.pd()

# 3o quadrante
t.pu()
t.goto(-200,-150)
t.color("#1f98cc")
t.stamp()
t.pd()

# 4o quadrante
t.pu()
t.goto(200,-120)
t.color("#22ba1a")
t.stamp()
t.pd()

mainloop()