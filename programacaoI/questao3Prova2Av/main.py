from util import printaBancoEmFormatoTabela
from util import mostraTabelasBanco
from util import insere
from util import criaBancoETabela
from util import pedeAlteracoes
from util import atualiza
from util import deleta
from util import busca

nomeBanco = input('Insira o nome do seu banco de dados: ')
mostraTabelasBanco(nomeBanco)
nomeTabela = input('Selecione/Crie uma tabela: ')
nomeBanco = 'database' if nomeBanco == '' else nomeBanco
nomeTabela = 'Table' if nomeTabela == '' else nomeTabela
criaBancoETabela(nomeBanco, nomeTabela)

while True:
  print(f'''+{"="*30}+
|{nomeTabela:^30}|
+{"="*30}+
|{"[1] - Inserir dados":<30}|
|{"[2] - Listar dados":<30}|
|{"[3] - Atualizar dados":<30}|
|{"[4] - Deletar dados":<30}|
|{"[5] - Buscar dados":<30}|
|{"[6] - Sair da tabela":<30}|
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
  elif opcao =='3':
    id = int(input('Insira o id que você quer alterar: '))
    alteracoes = pedeAlteracoes(nomeBanco, nomeTabela)
    atualiza(nomeBanco, nomeTabela, alteracoes, id)
  elif opcao == '4':  
    id = int(input('Insira o id que você quer deletar: '))
    deleta(nomeBanco, nomeTabela, id)    
  elif opcao == '5':
    pesquisa = input('Insira o que você quer buscar: ')
    busca(nomeBanco, nomeTabela, pesquisa)
  elif opcao == '6':
    mostraTabelasBanco(nomeBanco)
    print(f'''+{"="*30}+
|{"[1]- Sair do banco":<30}|
|{"[2]- Selecione/Crie uma tabela":<30}|
+{"="*30}+''')
    resp = input('Opção: ')
    if resp == '2':
      nomeTabela = input('Selecione uma tabela ou crie uma com um nome novo: ')
      criaBancoETabela(nomeBanco, nomeTabela)
    else:
      break    
  else:
    print('\033[1;31mErro: Essa opção não é válida\033[m')