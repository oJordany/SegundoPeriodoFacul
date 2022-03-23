def identificaEClassificaPG(sequencia):
    razao = sequencia[1]/sequencia[0]
    if razao != 0:
        for indice in range(2, len(sequencia)):
            if razao != sequencia[indice]/sequencia[indice-1]:
                return 'não é uma P.G.'
    if sequencia[1] > sequencia[0] and razao > 1:
        return 'P.G. Crescente para termos positivos'
    elif sequencia[1] > sequencia[0] and 0 < razao < 1:
        return 'P.G. Crescente para termos negativos'
    elif sequencia[1] == sequencia[0] and razao == 1:
        return 'P.G Constante'
    elif sequencia[1] < sequencia[0] and 0 < razao < 1:
        return 'P.G. Decrescente para termos positivos'
    elif sequencia[1] < sequencia[0] and razao > 1:
        return 'P.G. Decrescente para termos negativos'
    elif razao == -1:
        return 'P.G. Alternante'
    elif razao == 0:
        return 'P.G. Estacionária'

        
print(identificaEClassificaPG([]))
