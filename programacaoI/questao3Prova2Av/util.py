import sqlite3
from time import sleep

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

  for id in cur.execute(f'SELECT id FROM {nomeTabela}'):
    ultimoID = id[-1]

  dados = [ultimoID+1]        
  con.row_factory = sqlite3.Row
  cur = con.cursor()  
  cur.execute(f'SELECT * FROM {nomeTabela}')
  r = cur.fetchone()

  for i in range(1,6):
    if i != 3:
      dados.append(input(f'{r.keys()[i]}: '))
    else:
      dados.append(int(input(f'{r.keys()[i]}: ')))

  print(dados)
  cur.execute(f'''INSERT INTO {nomeTabela} VALUES ({dados[0]}, "{dados[1]}", "{dados[2]}", {dados[3]}, "{dados[4]}", "{dados[5]}")''')
  con.commit()
  con.close()
