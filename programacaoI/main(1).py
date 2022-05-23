import re

with open('texto37.txt', encoding='utf-8') as f:
  texto37 = f.read()  

with open('stopwords2.txt', encoding='utf-8') as f:
  stopwords2 = f.read()  

texto37 = re.sub(f'[^\w\s\-\']|\n', '', texto37)    
texto37 = re.split(' ', texto37)
stopwords2 = re.split(f'\n', stopwords2)

print('-'*500)

texto37 = list(filter(lambda palavra: palavra not in stopwords2, texto37))

print(texto37)


