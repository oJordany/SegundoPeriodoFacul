sequencia = list()
subconjuntoPrimos = list()
somaDosElementosPrimos = 0

indice = 0
while True:
    indice += 1
    try:
        sequencia.append(int(input(f'insira o elemento {indice} da sequencia [digite "X" para parar]: ')))  
    except:
        break

for elemento in sequencia:
    divisores = 0
    for anterior in range(elemento-1, 1, -1):
        if elemento % anterior == 0:
            divisores += 1
    if divisores == 0 and elemento != 1 and elemento != 0:
        subconjuntoPrimos.append(elemento)
        somaDosElementosPrimos += elemento
print(f'''O subconjunto dos elementos primos dessa sequência é: {subconjuntoPrimos}
A soma dos elementos do subconjunto dos números primos dessa sequência é: {somaDosElementosPrimos}''')