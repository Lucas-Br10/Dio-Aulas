
conta_normal = True
conta_universitaria = False

saldo = 2000
saque = 2500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial")
    else:
        print("Não foi possivel realizar o saqque, saldo insuficiente")

        """ 
        If aninhado quando vem um if seguido de if > if > elif > else
        """
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insufiente")
else:
    print("Sistema não reconheceu o tipo de conta, entre em contato com o seu gerente")

    # O ultimo else é caso os dois tipos de conta seja FALSE