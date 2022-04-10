n1, operacao, n2 = input('insira o seu calculo [separe tudo por espaço]: ').split(' ')
n1 = int(n1)
n2 = int(n2)

try:
    calc = {'+': f'Soma: {n1+n2}', '-': f'Subtracao: {n1-n2}', '*': f'Multiplicacao: {n1*n2}', '/': f'Divisao: {n1/n2}'}
    print(calc[operacao])
except ZeroDivisionError as erro:
    print(f'Nao eh possivel dividir um numero por 0 → {erro}')
except KeyError as erro:
    print(f'A operacao {erro} eh invalida') 
    