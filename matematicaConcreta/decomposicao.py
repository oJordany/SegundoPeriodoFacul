sequencia = list()
subconjuntoPrimos = list()

def somaElementosDe(sequencia):
    soma = 0
    for elemento in sequencia:
        soma += elemento
    return soma

# Inserindo os elementos da sequencia
indice = 0
while True:
    indice += 1
    try:
        sequencia.append(int(input(f'insira o elemento {indice} da sequencia [digite "X" para parar]: ')))  
    except:
        break
# Inserindo os valores de x e y que vão dividir a sequencia para ser decomposta
x = int(input('Insira um limite para o qual voce quer decompor a sequencia : '))
y = int(input('Insira outro limite para o qual voce quer decompor a sequencia : '))
if y > x:
    limiteMenor = x
    limiteMaior = y
else:
    limiteMenor = y
    limiteMaior = x

print(f'''A sequencia {sequencia} será decomposta nos seguintes intervalos:
elemento 1 - elemento {limiteMenor} 
elemento {limiteMenor + 1} - elemento {limiteMaior}
elemento {limiteMaior+1} - elemento {len(sequencia)}''')
# definindo os subintervalos e suas somas 
subIntervalo1 = {'sequencia': sequencia[0 : limiteMenor], 'soma': somaElementosDe(sequencia[0 : limiteMenor])}
subIntervalo2 = {'sequencia': sequencia[limiteMenor : limiteMaior], 'soma': somaElementosDe(sequencia[limiteMenor : limiteMaior])}
subIntervalo3 = {'sequencia': sequencia[limiteMaior : len(sequencia)+1], 'soma': somaElementosDe(sequencia[limiteMaior : len(sequencia)+1])}
# colocando os subintervalos em uma lista para que possam ser ordenados
subIntervalos = [subIntervalo1, subIntervalo2, subIntervalo3]
subIntervalos = sorted(subIntervalos, key= lambda subIntervalo: subIntervalo['soma'])

print(f'''Subconjuntos gerados pela decomposição em ordem crescente de acordo com o valor da soma de cada um:''')
for i in range(0, 3):
    print(subIntervalos[i]['sequencia'])
