#!/bin/bash

n = int(input("Digite um número inteiro positivo: "))

i = 1

while (i < n):
    a = i
    b = i + 1
    c = i + 2
    v = a*b*c
    if (v == n):
        print("É triangular. Numeros:",a,b,c)
    i+=1

        
