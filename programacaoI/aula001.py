# Desafio do prof + treinos
print(f'{" Aula 001 ":=^60}')
nomeCompleto = input('Insira o seu nome completo: ')
idade = int(input("insira a sua idade: "))
sexo = input("Sexo[M/F]: ").upper()[0]
print(f'Olá {nomeCompleto}, vc tem {idade} anos de idade e sexo {sexo}')
print(f'O seu nome tem {len("".join(nomeCompleto.split(" ")))} letras')


# Desafio do prof
entrada = input('Insira um valor: ')
while(entrada == ''):
  entrada = input('Insira um valor: ')
print(entrada)


# Teinando ...
try: 
  int(input('Insira um valor numérico: '))
except Exception as e:
  print('algo deu errado: ', e)
finally:
  print('Obrigado')

  
# Desafio do prof
frase = input('insira uma citação: ')
autor = input('quem disse isso? ')
print(autor, "disse","\"" ,frase,"\"")


# Algoritmo sequencia de Fibonacci
termo1 = 0
termo2 = 1
termos = int(input('Quantos termos da sequência de Fibonacci você quer ver? R:'))
for i in range(0,termos):
  if i == 0:
    print(termo1, end=' - ')
  elif i == termos-1:
    print(termo2)
  else:
    aux = termo1
    termo1 = termo2
    print(termo2, end = ' - ')
    termo2 += aux