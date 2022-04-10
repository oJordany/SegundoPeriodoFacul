sequencia = list()
subconjuntoPares = list()
somaDosElementosPares = 0

indice = 0
while True:
    indice += 1
    try:
        sequencia.append(int(input(f'insira o elemento {indice} da sequencia [digite "X" para parar]: ')))  
    except:
        break

for elemento in sequencia:
    if elemento % 2 == 0:
        subconjuntoPares.append(elemento)
        somaDosElementosPares += elemento

print(f'''Subconjunto dos números pares dessa sequência: {subconjuntoPares}
A soma do subconjunto dos números pares dessa seqência é igual a {somaDosElementosPares}''')
    