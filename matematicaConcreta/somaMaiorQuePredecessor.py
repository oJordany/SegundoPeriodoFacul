sequencia = list()
MaioresQuePredecessor = list()
somaMaioresQuePredecessor = 0

indice = 0
while True:
    indice += 1
    try:
        sequencia.append(int(input(f'insira o elemento {indice} da sequencia [digite "X" para parar]: ')))  
    except:
        break

for indiceAtual, elemento in enumerate(sequencia):
    indiceAnterior = indiceAtual - 1

    if indiceAtual > 0 and elemento > sequencia[indiceAnterior]:
        MaioresQuePredecessor.append(elemento)
        somaMaioresQuePredecessor += elemento

print(f'''O subconjunto dos elementos que são maiores do que os seus predecessores é: {MaioresQuePredecessor}
A soma do subconjunto de todos os números que são maiores do que o seu predecessor é: {somaMaioresQuePredecessor}''')