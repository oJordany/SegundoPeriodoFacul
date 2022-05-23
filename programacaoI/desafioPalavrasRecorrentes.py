#!/usr/bin/env python
# coding: utf-8

# # Pegando as palavras e filtrando 
# import re
# 
# with open('texto37.txt', encoding='utf-8') as f:
#   texto37 = f.read()  
# 
# with open('texto5.txt', encoding='utf-8') as f:
#   texto5 = f.read()  
# 
# with open('stopwords2.txt', encoding='utf-8') as f:
#   stopwords2 = f.read()  
# 
# texto37 = re.sub(f'[^\w\s\-\']|\n|\d', '', texto37)    
# texto37 = re.split(' ', texto37)
# texto5 = re.sub(f'[^\w\s\-\']|\n|\d', '', texto5)    
# texto5 = re.split(' ', texto5)
# 
# stopwords2 = re.split(f'\n', stopwords2)
# 
# texto37 = list(filter(lambda palavra: palavra not in stopwords2, texto37))
# texto5 = list(filter(lambda palavra: palavra not in stopwords2, texto5))

# # Lista texto37

# In[54]:


print(texto37)


# # Lista texto5

# In[55]:


print(texto5)


# # Criando listas no formato [[palavra, numero de ocorrências], ...]

# In[56]:


# Contando o número de cada palavra e colocando elas em uma lista com o respectivo número de ocorrência 
listaOcorrencia37 = [[texto37[0], texto37.count(texto37[0])]]

for palavra in texto37:
    contador = 0;
    for ocorrencia in listaOcorrencia37:
        if palavra in ocorrencia[0]:
            contador += 1
    if contador == 0:
        listaOcorrencia37.append([palavra, texto37.count(palavra)])
        
listaOcorrencia5 = [[texto5[0], texto5.count(texto5[0])]]

for palavra in texto5:
    contador = 0;
    for ocorrencia in listaOcorrencia5:
        if palavra in ocorrencia[0]:
            contador += 1
    if contador == 0:
        listaOcorrencia5.append([palavra, texto5.count(palavra)])        
        
# Ordenando a listaOcorrencia pelo numero de ocorrências 
listaOcorrencia37 = sorted(listaOcorrencia37, key = lambda ocorrencia: ocorrencia[1], reverse = True)
listaOcorrencia5 = sorted(listaOcorrencia5, key = lambda ocorrencia: ocorrencia[1], reverse = True)


# # listaOcorrencia37

# In[57]:


print(listaOcorrencia37)


# # listaOcorrencia5

# In[58]:


print(listaOcorrencia5)


# # Plotando os Gráficos

# In[59]:


#criando o eixo x e y dos gráficos
import matplotlib.pyplot as plt

x37 = [ocorrencia[0] for ocorrencia in listaOcorrencia37]
y37 = [ocorrencia[1] for ocorrencia in listaOcorrencia37]
x5 = [ocorrencia[0] for ocorrencia in listaOcorrencia5]
y5 = [ocorrencia[1] for ocorrencia in listaOcorrencia5]

# pegando somente as dez palavras mais frequentes
x37 = x37[0:10]
y37 = y37[0:10]
x5 = x5[0:10]
y5 = y5[0:10]

# Construindo os gráficos
figura = plt.figure(figsize=(23,10))
figura.suptitle('Palavras Mais Frequentes no texto37.txt e no texto5.txt')
figura.add_subplot(121)
# Gráfico do texto37
plt.bar(x37, y37, label='ocorrência das palavras')
plt.title('Palavras Mais Frequentes No texto37.txt')
plt.ylabel('Ocorrências')
plt.xlabel('Palavras')
plt.yticks([yi for yi in y37])
plt.legend()
# Gráfico do texto5
figura.add_subplot(122)
plt.bar(x5, y5, label='ocorrência das palavras')
plt.title('Palavras Mais Frequentes No texto5.txt')
plt.ylabel('Ocorrências')
plt.xlabel('Palavras')
plt.yticks([yi for yi in y5])
plt.legend()

# mostrando os gráficos
plt.show(figura)

