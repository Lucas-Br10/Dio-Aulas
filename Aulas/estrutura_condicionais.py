MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

Idade = int(input("Informe sua idade: "))

if Idade >= MAIOR_IDADE:
    print("Maior de idade, Pode tirar a CNH")

if Idade < MAIOR_IDADE:
    print("Ainda não pode tirar a CNH")

    # if: Avalia uma condição. Se for verdadeira, o bloco de código associado é executado. 

if Idade >= MAIOR_IDADE:
    print("Maior de idade, Pode tirar a CNH")
else:
    print("Ainda não pode tirar a CNH")

    # Captura todos os outros casos, ou seja, é executado se nenhuma condição anterior for verdadeira.

if Idade >= MAIOR_IDADE:
    print("Maior de idade, Pode tirar a CNH")

elif Idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teoricas, mas não pode fazer aulas praticas.")

else:
    print("Ainda não pode tirar a CNH")

    # elif (else if): É uma condição adicional caso a anterior seja falsa.