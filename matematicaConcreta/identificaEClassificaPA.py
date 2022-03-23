def identificaPA(sequencia):
    razao = sequencia[1] - sequencia[0]
    indice = 2
    while indice < len(sequencia):
        if razao != sequencia[indice] - sequencia[indice-1]:
            return 'não é uma P.A.'
        indice += 1
    if razao == 0:
        return 'é uma P.A. constante'
    elif razao < 0:
        return 'é uma P.A. decrescente'
    else:
        return 'é uma P.A. crescente'

print(identificaPA([2, 2, 2, 2]))
