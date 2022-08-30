#!/bin/python

n = int(input("Digite o valor de n: "))

fatorial = 1

while n > 0:
    fatorial = fatorial * n    
    n = n - 1     

print("O fatorial do número digitado é:",fatorial)