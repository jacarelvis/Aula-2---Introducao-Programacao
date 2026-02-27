# Programa calculadora Python
# Disciplina fundamentos da programação
# Data: 26/02/2026

import math

print("#########################################")
print("             Calculadora Python          ")
print("#########################################")

print("tecle a opção desejado e aperte ENTER")
print("1 - SOMA")
print("2 - SUBTRAÇÃO")
print("3 - POTENCIAÇÃO")
print("4 - RAIZADOR")
print("5 - MULTIPLICADOR")
print("6 - DIVISOR")

op = input ("Opção Desejada: ")
op = int(op)

if ( op < 1 or op > 6):
	print ("erro, coloque um número de 1 a 6")



if ( op == 1 ):
	a = input ("Entre com o valor de A: ")
	a = int(a)
	b = input ("Entre com o valor de B: ")
	b = int(b)
	print ("A soma é: ", a+b)

elif (op ==2):
	a = input ("Entre com o valor de A: ")
	a = int(a)
	b = input ("Entre com o valor de B: ")
	b = int(b)
	print ("A subtração é: ", a-b)

elif (op ==3):
	a = input ("Entre com o valor de A: ")
	a = int(a)
	b = input ("Entre com o valor de B: ")
	b = int(b)
	print ("A potenciação é: ", a**b)
elif (op ==4):
	a = input ("Entre com o valor de A: ")
	a = int(a)
	print ("A raizador é: ", math.sqrt(a))
elif (op ==5):
	a = input ("Entre com o valor de A: ")
	a = int(a)
	b = input ("Entre com o valor de B: ")
	b = int(b)
	print ("A potenciação é: ", a*b)
elif (op ==6):
	a = input ("Entre com o valor de A: ")
	a = int(a)
	b = input ("Entre com o valor de B: ")
	b = int(b)
	print ("O divisor é: ", a/b)


input()