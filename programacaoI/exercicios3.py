#-------------------------------------------------

#-------------  Algoritmo 181  -------------------

#-------------------------------------------------

soma = 0

for i in range(1, 101):
    soma += i
    if i != 100:
        print(i, end=' - ')
    else:
        print(i)
print(f'soma: {soma}')

#-------------------------------------------------

#-------------  Algoritmo 185  -------------------

#-------------------------------------------------

from math import sqrt

for i in range(1, 16):
    numero = int(input('Insira um numero: '))    
    if numero >= 0:
        print(sqrt(numero))
    else:
        print('Nao faco raiz de numero negativo')

#-------------------------------------------------

#-------------  Algoritmo 189  -------------------

#-------------------------------------------------

f1 = int(input('Entre com a temperatura maior em Fahrenheit: ')) 
f2 = int(input('Entre com a temperatura menor em Fahrenheit: '))       
dec = int(input('Entre com o decremento: ')) 
print(f'+{"-"*41}+')
print(f'|{"Fahrenheit":^20}|{"Celsius":^20}|')
print(f'+{"-"*20}+{"-"*20}+')
for t in range(f1, f2-1, -dec):
    c = 5 * (t - 32) / 9 
    print(f'|{t:^20}|{c:^20}|')
    if t != f2:
        print(f'|{"-"*20}+{"-"*20}|')
print(f'+{"-"*41}+')


#-------------------------------------------------

#-------------  Algoritmo 202  -------------------

#------------------------------------------------- 

num = int(input('Entre com um numero maior do que 15: '))
if num >= 15:
    for i in range(15, num+1, +15):
            print(i, end=' ')
else:
    print('NAO EXISTE!', end=' ')
print() 

#-------------------------------------------------

#-------------  Algoritmo 204  -------------------

#------------------------------------------------- 

num = int(input('Quantos numeros vc quer digitar? '))
for i in range(1, num+1):
    if i == 1:
        num1 = float(input('Digite um numero: '))
        maior = num1
    else:
        num1 = float(input('Digite um numero: '))
        if num1 > maior:
            maior = num1 

print('O maior numero que vc digitou eh: ', maior) 

#-------------------------------------------------

#-------------  Algoritmo 210  -------------------

#------------------------------------------------- 

a1 = int(input('Entre com o primeiro termo: '))
a2 = int(input('Entre com o segundo termo: '))
print(f'{a1} {a2}', end=' ')

for i in range(3, 11):
    if i % 2 == 0:
        termo = a2-a1
    else:
        termo = a2+a1
    print(termo, end=' ')
    a1 = a2 
    a2 = termo 
