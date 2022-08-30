#!/bin/python3

numero = int(input("Digite um número inteiro: "))
n = ((numero - (numero % 10)) // 10) % 10
print("O número digitado foi:", int(numero), "- O dígito das dezenas é:", int(n))