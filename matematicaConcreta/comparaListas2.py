def comparaSequenciasAleatoriamente():
    from random import randint
    global sequenciaA, sequenciaB

    indicesJaSorteados = []
    comandos = 0
    while True:
        indiceAleatorio = randint(0,99)   
        while indiceAleatorio in indicesJaSorteados:
            indiceAleatorio = randint(0,99)
            comandos += 1
        indicesJaSorteados.append(indiceAleatorio)
        comandos += 1
        if sequenciaA[indiceAleatorio] != sequenciaB[indiceAleatorio]:
            break
    return comandos


def comparaSequenciasEmOrdem():
    global sequenciaA, sequenciaB

    comandos = 0
    for indice, elemento in enumerate(sequenciaA):
        comandos += 1
        if elemento != sequenciaB[indice]:
            break
    return comandos


def trocaZeroPorUm():
    from random import randint
    global indicesSorteados
    global sequenciaA, sequenciaB

    indiceAleatorio = randint(0,99)
    while indiceAleatorio in indicesSorteados:
        indiceAleatorio = randint(0,99)
    indicesSorteados.append(indiceAleatorio)
    sequenciaA[indiceAleatorio] = 1



def criaSequencias():
    global sequenciaA, sequenciaB

    sequenciaA = []
    sequenciaB = []
    for i in range(0, 100):
        sequenciaA.append(0)
        sequenciaB.append(0)


comandosComparandoEmOrdem = []
comandosComparandoAleatoriamente = []
indicesSorteados = []
while len(indicesSorteados) != 100:
    criaSequencias()
    trocaZeroPorUm()
    comandosComparandoEmOrdem.append(comparaSequenciasEmOrdem())
    comandosComparandoAleatoriamente.append(comparaSequenciasAleatoriamente())
print(comandosComparandoEmOrdem)
print(comandosComparandoAleatoriamente)
