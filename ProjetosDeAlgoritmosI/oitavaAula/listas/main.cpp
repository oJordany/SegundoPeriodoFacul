#include <iostream>
#include <cstdlib>
#include "lista.h"

using namespace std;

int main(void){
  TipoLista* list;
  list = InicializaLista();
  cout << "lista vazia?: " << Vazia(list) << endl;
  TipoItem* item; 
  item=(TipoItem*)malloc(sizeof(TipoItem));
  item->valor = 10;
  cout << "valor a ser inserido: " << item->valor  << endl;
  Insere(item, list);
  item->valor = 20;
  cout << "valor a ser inserido: " << item->valor  << endl;
  Insere(item, list);
  cout << "lista vazia?: " <<  Vazia(list) << endl;
  cout << "Tamanho da lista: " << Tamanho_lista(list)  << endl;

  cout << "consulta pelo valor: 10"  << endl;
  Busca(10, list);
  cout << "Imprimir a Lista" << endl;
  Imprime(list);
  cout << "Remover na posicao: 0" << endl;
  cout << Retira(0, list)->valor << endl;
  cout << "tamanho da lista: " << Tamanho_lista(list) << endl;
  cout << "Faz a lista ficar vazia" << endl;
  FLVazia(list);
  cout << "tamanho da lista: " << Tamanho_lista(list) << endl;
  cout << "lista vazia?: " <<  Vazia(list) << endl;
  
  /*Inserindo elementos na lista*/
  item->valor = 1;
  Insere(item, list);
  Insere(item, list);
  Insere(item, list);
  Insere(item, list);
  item -> valor = 0;
  Insere(item, list);
  Insere(item, list);
  Insere(item, list);
  item -> valor = 5;
  Insere(item, list);
  Insere(item, list);
  Insere(item, list);
  Insere(item, list);
  Insere(item, list);
  Insere(item, list);
  Insere(item, list);
  item -> valor = -1;
  Insere(item, list);
  cout << endl;
  cout << "Mostrando como a lista está:" << endl;
  Imprime(list);
  cout << "Usando a nossa funcao que mostra o elemento com mais e menos ocorrencias: " << endl;
  MaisEMenosVezes(list);
  /*Vamos usar a mesma lista, com os mesmos elementos*/ 
  cout << endl << "Mostrando como a lista esta: " << endl;
  Imprime(list);
  cout << endl << "Usando a nossa fucao que mostra o elemento mais a sua ocorrencia: " << endl;
  TipoLista* L2 = ListaElemECount(list); 
  Imprime(L2, true);
}

