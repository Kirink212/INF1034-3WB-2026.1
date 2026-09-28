from random import choice
# 1o passo: gerar aleatoriamente a palavra
lista = ["banana", "laranja", "maca", "abacaxi", "kiwi"]

palavra_aleatoria = choice(lista)
palavra_oculta = "_ " * len(palavra_aleatoria)

print(palavra_oculta, "\n\n")

letra = input("Digite uma letra da palavra:")

if letra in palavra_aleatoria:
    palavra_aux = ""
    for i in range(len(palavra_aleatoria)):
        if letra == palavra_aleatoria[i]:
            # substituir o '_ ' na palavra oculta pela letra
            palavra_aux += letra + ' '
        else:
            palavra_aux += palavra_oculta[2*i] + ' '
else:
    print("Errou")

palavra_oculta = palavra_aux

print(palavra_oculta, "\n\n")
