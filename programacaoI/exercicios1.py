# #-------------------------------------------------

# #--------------  Algoritmo 23 --------------------

# #-------------------------------------------------

# a = int(input('Digite numero de 3 casas: '))
# d = a % 100 // 10
# print(f'Algarismo da casa das dezenas: {d}')
# print('\n')

# #-------------------------------------------------

# #--------------  Algoritmo 25 --------------------

# #-------------------------------------------------

# data = int(input('Digite data no formato DDMMAA: '))
# dia = data // 10000
# mes = data % 10000 // 100
# ano = data % 100
# print(f'DIA: {dia}')
# print(f'MES: {mes}')
# print(f'ANO: {ano}')
# print('\n')

# #-------------------------------------------------

# #--------------  Algoritmo 34 --------------------

# #-------------------------------------------------

# numero = int(input('entre com um numero: '))
# ant = numero - 1
# suc = numero + 1
# print(f'o sucessor eh {suc} e o antecessor eh {ant}')
# print('\n')

# #-------------------------------------------------

# #--------------  Algoritmo 38 --------------------

# #-------------------------------------------------

# num = float(input('entre com um numero com ponto: '))
# print(f'A terça parte eh: {(num/3):.2f}')
# print('\n')

# #-------------------------------------------------

# #--------------  Algoritmo 39 --------------------

# #-------------------------------------------------

# nota1 = float(input('digite 1a nota: '))
# nota2 = float(input('digite 2a nota: '))
# media = (nota1 + nota2)/2
# print(f'media: {media:.2f}')
# print('\n')

# #-------------------------------------------------

# #--------------  Algoritmo 40 --------------------

# #-------------------------------------------------

# val1 = int(input('entre com o dividendo: '))
# val2 = int(input('entre com o divisor: '))
# quoc = val1 // val2
# rest = val1 % val2
# print('\n\n\n')
# print(f'dividendo: {val1}')
# print(f'divisor: {val2}')
# print(f'quociente: {quoc}')
# print(f'resto: {rest}')
# print('\n')

# #-------------------------------------------------

# #--------------  Algoritmo 41 --------------------

# #-------------------------------------------------

# a = float(input('entre com 1 numero: '))
# b = float(input('entre com 2 numero: '))
# c = float(input('entre com 3 numero: '))
# d = float(input('entre com 4 numero: '))
# mp = (a*1 + b*2 + c*3 + d*4)/10
# print(f'media ponderada: {mp}')
# print('\n')

# #-------------------------------------------------

# #--------------  Algoritmo 42 --------------------

# #-------------------------------------------------

from math import sin, cos, tan, pi
angulo = float(input('digite um angulo em graus: '))
rang = angulo*pi/180
print(f'seno: {sin(rang)}')
print(f'cosseno: {cos(rang)}')
if angulo%90 != 0: 
    print(f'tangente: {(tan(rang))}')
else:
    print(f'tangente: nao existe')
if sin(rang) != 0 and cos(rang) != 0 and tan(rang) != 0:
    print(f'cossecante: {(1/sin(rang))}')
    print(f'secante: {(1/cos(rang))}')
    if angulo%90 != 0:
        print(f'cotangente: {(1/tan(rang))}')
    else:
        print(f'cotangente: nao existe')
print('\n')
