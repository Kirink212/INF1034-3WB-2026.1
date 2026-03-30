from turtle import *
from time import sleep

def desenha_retangulo(x, y, larg, alt, color):
    t.pu()
    t.goto(x, y)
    t.pd()

    t.begin_fill()
    t.fillcolor(color)
    for _ in range(2):
        t.fd(larg)
        t.rt(90)
        t.fd(alt)
        t.rt(90)
    t.end_fill()

def desenha_bandeira_franca():
    desenha_retangulo(-200, 200, 50, 150, "#002153")
    desenha_retangulo(-150, 200, 50, 150, "white")
    desenha_retangulo(-100, 200, 50, 150, "#CF0921")

t = Turtle()

desenha_bandeira_franca()
sleep(5)
t.clear()

mainloop()