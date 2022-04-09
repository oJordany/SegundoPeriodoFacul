# As duas aulas passadas foram perdidas no replit kkskksk
print(f'{"Conversão de moedas":=^60}')
print('''1. euro para dólar
2. dólar para euro''')
opcao = int(input('escolha uma opção: '))
taxa_euro = 1.09
taxa_real = 0.21
if opcao == 1:
  euro = int(float(input('Insira o valor em euro q vc quer converter: ')))
  print(f'{euro:.2f} euro/euros é igual a ${euro*taxa_euro:.2f}')
elif opcao == 2: 
  real = float(input('Insira o valor em reais q vc quer converter: '))
  print(f'{real:.2f} real/reais é igual a ${real*taxa_real:.2f}')
else:
  print('Ops! Opção inválida')

# Com um dicionário
moedas = {'dolar': 1.09, 
          'real': 0.21, 
          'franco': 1.02, 
          'libra': 0.83, 
          'iene': 134.90}
euro = int(float(input('Insira o valor em euro q vc quer converter: ')))
opcao = input('escolha uma opção para converter [dolar/real/franco/libra/iene]: ')
print(f'{euro} euro/euros é igual a {moedas[opcao]*euro:.2f} em {opcao}')

print(f'{"Rendimento de um investimento (juros simples)":=^60}')
valor_principal = float(input('Insira o valor principal: '))
taxa_de_rendimento = int(input('Insira a taxa de rendimento (a.a.) em porcentagem: '))
numero_de_anos = int(input('Insira o número de anos: '))
rendimento = (valor_principal * taxa_de_rendimento/100) * numero_de_anos 
montante = (valor_principal * taxa_de_rendimento/100) * numero_de_anos + valor_principal

print(f'Depois de {numero_de_anos} anos, vc vai ter R${montante:.2f}')
print(f'Rendeu R${rendimento:.2f}')

print(f'{"Rendimento de um investimento (juros Compostos)":=^60}')
valorPrincipal = float(input('Insira o valor principal: '))
aux = valorPrincipal
taxaDeRendimento = int(input('Insira a taxa de rendimento (a.a.) em porcentagem: '))
anos = int(input('Insira o número de anos: '))
for i in range (0, anos):
  valorPrincipal = (valorPrincipal * taxaDeRendimento/100) + valorPrincipal
print(f'Depois de {anos} anos, vc vai ter R${valorPrincipal:.2f}')
print(f'Rendeu R${valorPrincipal - aux:.2f}')


print(f'{" Calcula Imposto do Produto ":=^60}')
valor = float(input('Qual o valor do pedido: '))
estado = input('Insira o Estado: ').upper()
if estado == 'WI' or estado == 'WINSCONSIN':
  taxa = (5.5/100) * valor
  print(f'''♦subtotal: ${valor:.2f}
♦taxa: ${taxa:.2f}
♦total: ${valor+taxa:.2f}''')
else:
  print(f'♦O total é ${valor:.2f}')



import getpass
print(f"{'Simulador de Login':=^60}")
logins = {
  'fulano': 'enable',
  'ciclano': 'enable123',
  'beltrano': 'enable0123'
}
while True:
  usuario = input('insira o seu nome de usuario: ')
  senha = getpass.getpass('insira a sua senha: ')
  if usuario not in logins:
    print('\033[1;31mOps! usuário não encontrado\033[m')
  elif senha == logins[usuario]:
    print('\033[1;32mBem vindo!\033[m')
    break
  else:
    print('\033[1;31mOps! Senha incorreta\033[m')