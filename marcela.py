#  Crie um programa que leia dois números e mostre a soma, a
# subtração, a multiplicação e a divisão entre ele

num1 = int(input('Insira o primeiro número: '))
num2 = int(input('Insira o segundo número: '))

def soma(a,b):
    soma = a + b 
    print(soma)

def subtração(a,b):
    sub = a - b
    print(sub)

def multiplicar(a,b):
    mult = a * b
    print(mult)

def divisao(a,b):
    div = a / b
    print(div)

soma(num1, num2)  
subtração(num1, num2)
multiplicar(num1, num2)
divisao(num1, num2)