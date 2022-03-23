def comparaSequencias(sequencia1, sequencia2):
    iguais = True
    cont = 0
    if len(sequencia1) != len(sequencia2):
        iguais = False
    else:
        for indice, elemento in enumerate(sequencia1):
            if elemento != sequencia2[indice]:
                iguais = False
                break
    print('São iguais') if iguais else print('São diferentes')


comparaSequencias([1,2,3,4], [1,2,0,4])