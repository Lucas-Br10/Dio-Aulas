saldo = 1000
limite = 500

print(saldo is limite)
# False
# Não ocupam a mesma região de memória 

print(saldo is not limite)
# True
# Realmente não ocupam a mesma região de memória 

valor1 = 1000
valor2 = 1000

print(valor1 is valor2)
# True
# São da mesma região de memória

print(valor1 is not valor2)
# False
# Não são da mesma região de memória  