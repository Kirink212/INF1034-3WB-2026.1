from turtle import *
from random import randint

t = Turtle()

def soma_2(x):
    return x + 2

def saudacao(nome):
    print(f"Olá {nome}, tudo bem?")

# retorno = saudacao("Luís Bicalho")
# print(retorno)

saudacao("Luís Bicalho")

def desenha_quadrado(x, y, tamanho, color):
    t.pu()
    t.goto(x, y)
    t.pd()
    t.begin_fill()
    t.fillcolor(color)
    for _ in range(4):
        t.fd(tamanho)
        t.rt(90)
    t.end_fill()

desenha_quadrado(200, 300, 100, "red")

# Desenhar um quadrado
# t.pu()
# t.goto(-200, -300)
# t.pd()
# t.begin_fill()
# t.fillcolor("blue")
# for _ in range(4):
#     t.fd(100)
#     t.rt(90)
# t.end_fill()

desenha_quadrado(-200, -300, 50, "blue")

color = textinput("Escolhar a cor", "Digite a cor desejada:")
x = randint(100, 300)
y = randint(100, 300)
desenha_quadrado(x, y, 200, color)

mainloop()