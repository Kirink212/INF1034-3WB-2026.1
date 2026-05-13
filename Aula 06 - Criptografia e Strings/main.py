def valida_email(email):
    return email[-8:] == "@puc.com"

print(valida_email("lfbicalho@hotmail.com"))

def possuiMaiuscula(palavra):
    for letra in palavra:
        if 'A' <= letra <= 'Z': # letra.isupper()
            return True
    return False

def possuiMinuscula(palavra):
    for letra in palavra:
        if 'a' <= letra <= 'z': # letra.islower()
            return True
    return False

def possuiNumero(palavra):
    for caracter in palavra:
        if '0' <= caracter <= '9':
            return True
    return False

print(possuiMaiuscula("abc@1234"))
print(possuiMinuscula("ABC@1234"))
print(possuiMinuscula("Abc@1234"))

def valida_senha(senha):
    check_tamanho = len(senha) >= 8
    check_maiuscula = possuiMaiuscula(senha)
    check_minuscula = possuiMinuscula(senha)
    check_numero = possuiNumero(senha)
    return check_tamanho and check_maiuscula and check_minuscula and check_numero

print("\nTestando a 'valida_senha':")
print(valida_senha("ABc@1234"))
print(valida_senha("BCA@1234"))
print(valida_senha("def@1234"))
print(valida_senha("def@abcd"))
print(valida_senha("Def@123"))

def criptografa_senha(senha):
    senha_cripto = ""
    for char in senha:
        if char.isdigit():
            # Copiar lógica do maiúsculo, trocando ref para '0'
            # e o 26 para 10 
            pass
        elif 'A' <= char <= 'Z':
            ref = ord('A') # 65
            ascii_char = ord(char) # Etapa 1
            pos_alpha = ascii_char - ref # Etapa 2
            pos_cesar = pos_alpha + 3 # Etapa 3
            pos_cesar = pos_cesar % 26 # Etapa 4
            letra_cesar = chr(ref + pos_cesar) # Etapa 5
            senha_cripto += letra_cesar
        elif 'a' <= char <= 'z':
            # Copiar lógica do maiúsculo, trocando ref para 'a'
            pass
        else:
            senha_cripto += char
    return senha_cripto

print(criptografa_senha("ZARALHAR@"))