#!/bin/python3

n = int(input("Digite o valor de n: "))
d = int(input("Digite um numero de [0,9]: "))
num = n
count = 0

while (n != 0):
    resto = n % 10 
    if (resto == d):
        count+=1
    n = n // 10

print("O dígito", d, "ocorre", count,"vezes em", num)