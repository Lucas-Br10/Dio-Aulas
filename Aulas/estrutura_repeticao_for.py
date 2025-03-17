texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        # .upper (Tranforma a letra minuscula em maiuscula)
        print(letra, end="")

else:
    print() # adiciona uma quebra de inhas
    print("Executa no final do laço")

for numero in range(0, 51, 5):
    print(numero, end=" ")