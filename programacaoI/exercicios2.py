#-------------------------------------------------

#--------------  Algoritmo 88  -------------------

#-------------------------------------------------
print(f'{"*"*13:^62}\n{"*CALCULADORA*":^62}\n{"*"*13:^62}\n{"+ para somar ":^62}\n{"- para subtrair":^63}\n{"* para multiplicar":^67}\n{"/ para dividir":^62}')

resp = input('\t\t\tDigite a opção: ').strip()[0]
num1 = float(input('Digite o 1º número com ponto: '))
num2 = float(input('Digite o 2º número com ponto: '))

if resp == '+':
    print(f'SOMA DE {num1} + {num2} = {num1 + num2:.2f}')
elif resp == '-':
    print(f'SUBTRAÇÃO DE {num1} - {num2} = {num1 - num2:.2f}')
elif resp == '*':
    print(f'MULTIPLICAÇÃO DE {num1} * {num2} = {num1*num2:.2f}')
elif resp == '/':
    try:
        print(f'DIVISÃO DE {num1} / {num2} = {num1/num2:.2f}')
    except ZeroDivisionError as erro:
        print(f'NÃO É POSSÍVEL DIVIDIR UM NÚMERO POR ZERO → {erro}')
else:
    print('OPÇÃO INDISPONÍVEL!')

print('\n')

#-------------------------------------------------

#--------------  Algoritmo 97  -------------------

#-------------------------------------------------

numero = int(input('Digite um número: '))
if numero % 10 == 0:
    print(f'{numero} é múltiplo de 10')
elif numero % 2 == 0:
    print(f'{numero} é múltiplo de 10')
elif numero % 5 == 0:
    print(f'{numero} é múltiplo de 5')
else:
    print(f'{numero} não é múltiplo de 2 nem de 5')

print('\n')

# -------------------------------------------------

# -------------  Algoritmo 100  -------------------

# -------------------------------------------------

num = int(input('numero de 4 algarismos: '))
c = num // 100
if c % 4 == 0:
    print(f'O número {c} é múltiplo de 4')
else:
    print(f'O número {c} não é múltiplo de 4')

print('\n')

#-------------------------------------------------

#-------------  Algoritmo 108  -------------------

#-------------------------------------------------

from calendar import c


nome = input('Digite um nome: ').strip()
listaNome = nome.split(' ')
if listaNome[0] == 'JOSÉ'or listaNome[0] == 'José' or listaNome[0] == 'josé':
    print(nome)

print('\n')

#-------------------------------------------------

#-------------  Algoritmo 119  -------------------

#-------------------------------------------------

num1 = float(input('digite o 1º número: '))
num2 = float(input('digite o 2º número: '))
num3 = float(input('digite o 3º número: '))

if num1 > num2:
    aux = num1
    num1 = num2
    num2 = aux
if num1 > num3:
    aux = num1
    num1 = num3
    num3 = aux
if num2 > num3:
    aux = num2
    num2 = num3
    num3 = aux
print(f'Ordem Decrescente: {num3}, {num2}, {num1}')

print('\n')

# -------------------------------------------------

# -------------  Algoritmo 122  -------------------

# -------------------------------------------------

a = float(input('digite o primeiro lado: '))
b = float(input('digite o segundo lado: '))
c = float(input('digite o terceiro lado: '))

if a < b + c and b < a + c and c < a + b:
    print('Podem ser lados de um triangulo')
else:
    print('Não podem ser lados de um triângulo')

print('\n')

#-------------------------------------------------

#-------------  Algoritmo 123  -------------------

#-------------------------------------------------

a = float(input('digite o primeiro lado: '))
b = float(input('digite o segundo lado: '))
c = float(input('digite o terceiro lado: '))

if a < b + c and b < a + c and c < a + b:
    if  a == b and a == c:
        print('Triangulo equilatero')
    elif a == b or a == c or b == c:
        print('Triangulo isosceles')
    else:
        print('Triangulo escaleno')
else:
    print('As medidas não formam um triângulo')
    
print('\n')

#-------------------------------------------------

#-------------  Algoritmo 124  -------------------

#-------------------------------------------------

a = float(input('digite o primeiro lado: '))
b = float(input('digite o segundo lado: '))
c = float(input('digite o terceiro lado: '))

if a < b + c and b < a + c and c < a + b:
    if a > b and a > c:
        maior = a ** 2
        lados = b ** 2 + c **2
    elif b > c:
        maior = b ** 2 
        lados = a ** 2 + c ** 2
    else:
        maior = c ** 2 
        lados = b ** 2 + a ** 2
    
    if maior == lados:
        print('Triângulo Retângulo')
    elif maior > lados:
        print('Triângulo Obtusângulo')
    else:
        print('Triâgulo Acutângulo')
else:
    print('As medidas não formam um triângulo')

print('\n')

#-------------------------------------------------

#-------------  Algoritmo 138  -------------------

#-------------------------------------------------

meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

numeroMes = int(input('Digite um numero de 1 - 12: '))

try:
    print(meses[numeroMes-1])
except:
    print(f'não existe mês correspondente ao número {numeroMes}')

print('\n')
