#!/bin/python3

n = int(input("Valor de n: "))
par = impar = i = 0

while(i < n):
	numero = int(input())

	if (numero % 2 == 0):
		par += 1
	else:
		impar += 1
		
	i += 1

print("Pares:", par, "Impares:", impar)