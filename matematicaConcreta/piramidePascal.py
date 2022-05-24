def fatorialDe(numero):
    if numero == 0:
        return 1
    else:
        fatorial = 1
        while numero > 1:
            fatorial *= numero
            numero -= 1
        return fatorial


print(f'{" PIRAMIDE DE PASCAL ":=^70}')
coeficienteFinal = int(input('insira ate qual coeficiente binomial vc deseja ver na piramide: '))
print('='*70)
for r in range(0, coeficienteFinal+1):
    for k in range(0, r+1):
        coeficienteBinomial = int(fatorialDe(r)/(fatorialDe(k)*fatorialDe(r-k)))
        print(f'{coeficienteBinomial:<6}', end='')     
    print()    