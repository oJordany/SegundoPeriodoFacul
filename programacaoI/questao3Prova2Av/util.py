import sqlite3
from time import sleep
from random import randint


def mostraTabelasBanco(nomeBanco):
  con = sqlite3.connect(f'{nomeBanco}.db')
  cur = con.cursor()
  cur.execute('SELECT name from sqlite_master where type= "table"')
  tabelasDoBanco = cur.fetchall()
  print('\n')
  if tabelasDoBanco == []:
    print('Banco vazio')
  else:
    print(f'TABELAS DE \033[1;32m{nomeBanco}\033[m:')
    for tabela in tabelasDoBanco:
      cor = randint(31,39)
      print(f'\033[1;{cor}m{tabela[0]}\033[m', end = '   ')
  print('\n')
def criaBancoETabela(nomeBanco, nomeTabela):
  con = sqlite3.connect(f'{nomeBanco}.db')
  cur = con.cursor()

  try:
    cur.execute(f'''CREATE TABLE {nomeTabela}
               (id integer, titulo text, autor text, ano integer, sinopse text, editora text)''')
    cur.execute(f'INSERT INTO {nomeTabela} VALUES (0, NULL, NULL, NULL, NULL, NULL)')
    print(f'Criando tabela {nomeTabela}...')
    sleep(2)
  except:
    print(f'Acessando tabela {nomeTabela}...')
    sleep(2)
  con.commit()
  con.close()


def printaListaEmFormatoTabela(lista):
  #Encontrando o maior membro da tabela
  biggestMember= 0;
  
  for row in lista:
    for data in row:
      if len(str(data)) > biggestMember:
        biggestMember = len(str(data))
         
  biggestMember += 3;

  # Table Header e Table Body
  for l, row in enumerate(lista):
    for i, data in enumerate(row):
      if i != len(row) - 1:
        print(f'{data}{" "*(biggestMember-len(str(data)))}|', end='')
      else:
        print(f'{data}{" "*(biggestMember-len(str(data)))}')
    if l == 0:
      print('-'*biggestMember*len(row))


def printaBancoEmFormatoTabela(baseDeDados, nomeTabela, order=''):
  # Tratando o order
  if order != '':
    order = f'ORDER BY {order}'
  else:
    order = ''
  # Usando o sqlite 3
  con = sqlite3.connect(f'{baseDeDados}.db')
  con.row_factory = sqlite3.Row
  cur = con.cursor()
  cur.execute(f'SELECT * FROM {nomeTabela}')
  r = cur.fetchone()
  # Encontrando o maior membro da tabela
  biggestMember= 0
  
  for key in r.keys():
    if len(str(key)) > biggestMember:
      biggestMember = len(str(key))

  
  for row in cur.execute(f'SELECT * FROM {nomeTabela}'):
    for data in row:
      if len(str(data)) > biggestMember:
        biggestMember = len(str(data))
        
  biggestMember += 3

  # Table Header
  for i, key in enumerate(r.keys()):
    if i != len(r.keys()) - 1:
      print(f'{key}{" "*(biggestMember-len(key))}|', end='')
    else:
      print(f'{key}{" "*(biggestMember-len(key))}', end='')
  
  print()
  print('-'*((biggestMember)*len(r.keys())+len(r.keys())-1))

  # Table Body
  for row in cur.execute(f'SELECT * FROM {nomeTabela} {order}'):
    if row[0] > 0:
      for i in range(0, len(row)):
        if i != len(row) - 1:
          print(f'{row[i]}{" "*(biggestMember-len(str(row[i])))}|', end='')
        else:
          print(f'{row[i]}{" "*(biggestMember-len(str(row[i])))}')
  
  print()
  con.close()


def insere(baseDeDados, nomeTabela):
  con = sqlite3.connect(f'{baseDeDados}.db')
  cur = con.cursor()

  cur.execute(f'SELECT id FROM {nomeTabela}')
  ids = cur.fetchall()
  if ids == []:
    cur.execute(f'INSERT INTO {nomeTabela} VALUES (0, NULL, NULL, NULL, NULL, NULL)')
  cur.execute(f'SELECT id FROM {nomeTabela}')
  ultimoID = cur.fetchall()[-1][0]  

  dados = [ultimoID+1]        
  con.row_factory = sqlite3.Row
  cur = con.cursor()  
  cur.execute(f'SELECT * FROM {nomeTabela}')
  r = cur.fetchone()

  for i in range(1,6):
    if i != 3:
      dados.append(input(f'{r.keys()[i]}[ENTER para Vazio]: '))
    else:
      try:
        dados.append(int(input(f'{r.keys()[i]}: ')))
      except:
        dados.append('')
  execute = f'INSERT INTO {nomeTabela} VALUES ('
  for i in range(0,6):
    if type(dados[i]) == int:
      execute += f'''{dados[i]}, '''
    elif dados[i] == '':
      execute += f'''NULL, '''
    else:
      execute += f'''"{dados[i]}", '''
  execute = list(execute)
  execute[-2] = ')'
  execute = ''.join(execute)
  cur.execute(execute)
  con.commit()
  con.close()


def atualiza(baseDeDados, nomeTabela, alteracoes, id):
  con = sqlite3.connect(f'{baseDeDados}.db')
  cur = con.cursor()
  alteracoesStr =''
  contador = 1
  for dado, alteracao in alteracoes.items():
    if contador < len(alteracoes):
      if type(alteracao) == str:
        alteracoesStr += f'''{dado} = "{alteracao}", '''
      elif alteracao == 'NULL':
        alteracoesStr += f'''{dado} = {alteracao} '''
      else:
        alteracoesStr += f'''{dado} = {alteracao}, '''
    else:
      if type(alteracao) == str:
        alteracoesStr += f'''{dado} = "{alteracao}" '''
      elif alteracao == 'NULL':
        alteracoesStr += f'''{dado} = {alteracao} '''
      else:
        alteracoesStr += f'''{dado} = {alteracao} '''
    contador += 1
  cur.execute(f'''UPDATE {nomeTabela} SET {alteracoesStr} WHERE id = {id};''')
  print('\033[1;32mDados Atualizados Com Sucesso...\033[m')
  con.commit()
  con.close()


def pedeAlteracoes(baseDeDados, nomeTabela):
  con = sqlite3.connect(f'{baseDeDados}.db')
  con.row_factory = sqlite3.Row
  cur = con.cursor()
  cur.execute(f'SELECT * FROM {nomeTabela}')
  r = cur.fetchone()
  alteracoes = dict()
  for indice in r.keys():
    try:
      if indice != 'id':
        alteracao = input(f'Insira o(a) novo(a) {indice} ou aperte ENTER para mantê-lo(a): ') if indice != 'ano' else int(input(f'Insira o(a) novo(a) {indice} ou aperte ENTER para mantê-lo(a): '))      
      if alteracao != '':
        alteracoes[indice] = alteracao
    except:
      continue
  return alteracoes


def deleta(baseDeDados, nomeTabela, id):
  con = sqlite3.connect(f'{baseDeDados}.db')
  cur = con.cursor()
  cur.execute(f'''DELETE FROM {nomeTabela} WHERE id = {id}''')
  print('\033[1;35mDados Deletados Com Sucesso...\033[m')
  con.commit()
  con.close()


def busca(baseDeDados, nomeTabela, substring):
  con = sqlite3.connect(f'{baseDeDados}.db')
  cur = con.cursor()
  con.row_factory = sqlite3.Row
  curRow = con.cursor()
  curRow.execute(f'''Select * FROM {nomeTabela}''')
  r = curRow.fetchone()
  dadosEncontrados = [r.keys()]
  for indice in r.keys():
    dadosIndice = list()  
    if indice != 'id':
      for palavra in cur.execute(f'''SELECT {indice} FROM {nomeTabela}'''):    
        dadosIndice.append(palavra[0])
      for palavra in dadosIndice:
        if palavra != None and substring.lower() in str(palavra).lower():
          if type(palavra) == str:
            cur.execute(f'''SELECT * FROM {nomeTabela} WHERE {indice} = "{palavra}"''')
          else:
            cur.execute(f'''SELECT * FROM {nomeTabela} WHERE {indice} = {palavra}''')
          dados = cur.fetchone()
          if dados not in dadosEncontrados:
            dadosEncontrados.append(dados)
  
  printaListaEmFormatoTabela(dadosEncontrados)
          