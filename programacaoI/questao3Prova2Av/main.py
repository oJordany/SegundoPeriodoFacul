from util import printaBancoEmFormatoTabela
from util import insere
from util import criaBancoETabela

nomeBanco = input('Insira o nome do seu banco de dados: ')
nomeTabela = input('Insira o nome da sua tabela: ')
nomeBanco = 'database' if nomeBanco == '' else nomeBanco
nomeTabela = 'Table' if nomeTabela == '' else nomeTabela

criaBancoETabela(nomeBanco, nomeTabela)


while True:
  print(f'''+{"="*30}+
|{nomeTabela:^30}|
+{"="*30}+
|{"[1] - Inserir dados":<30}|
|{"[2] - Listar dados":<30}|
|{"[3] - Sair":<30}|
+{"="*30}+''')
  opcao = input('Opção: ').strip()
  if opcao == '1':
    insere(nomeBanco, nomeTabela)
  elif opcao == '2':
    print(f'''+{"="*30}+
|{"ORDEM DE LISTAGEM":<30}|
+{"="*30}+
|{"[1] - id":<30}|
|{"[2] - titulo":<30}|
|{"[3] - autor":<30}|
|{"[4] - ano":<30}|
|{"[5] - sinopse":<30}|
|{"[6] - editora":<30}|
+{"="*30}+''')
    ordem = input('Selecione a ordem desejada: ').strip().lower()
    print()
    opcoesOrdem = {
        '1': 'id',
        '2': 'titulo',
        '3': 'autor',
        '4': 'ano',
        '5': 'sinopse',
        '6': 'editora'
    }
    try:
        ordem = opcoesOrdem[ordem]
    except:
        ordem = 'id'
    
    printaBancoEmFormatoTabela(nomeBanco, nomeTabela, ordem)
  elif opcao == '3':
    break
  else:
    print('\033[1;31mErro: Essa opção não é válida\033[m')