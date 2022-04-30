#include <iostream>
#include <cstdlib>
#include "lista.h"

using namespace std;

/* Inicializa uma lista */
TipoLista* InicializaLista(){
  TipoLista* lista = (TipoLista*)malloc(sizeof(TipoLista));
  return lista;
}

/* Faz a lista ficar vazia */
void FLVazia (TipoLista* Lista) {
  Lista->Primeiro = InicioVetor;
  Lista->Ultimo = Lista->Primeiro; 
}

/*Verifica se a lista está vazia*/
int Vazia (TipoLista* Lista){
  return (Lista->Primeiro == Lista->Ultimo); 
}


/* Insere x após o último elemento da lista */
void Insere (TipoItem* x, TipoLista *Lista) {
  if (Lista ->Ultimo >= MaxTam)
    cout << "Lista está cheia" << endl;
  else{ 
    Lista ->Item[Lista->Ultimo] = *x; 
    Lista->Ultimo++;
  } 
}


TipoItem* Busca(int chave, TipoLista* lista){
  for(int i = 0; i < lista->Ultimo; i++){
    if(lista->Item[i].valor == chave){
      cout << "Item existe" << endl;
      return &lista->Item[i];
    }else{
      cout << "Item não encontrado" << endl;
      return NULL;
    }
  }
  return NULL;
}

int Tamanho_lista(TipoLista* Lista){
  if (Lista == NULL)
    return -1;
  else 
    return Lista->Ultimo;
}

/*Retorna o item x que está na posição p da lista, retirando-o da lista e deslocando os itens a partir da posição p+1 para as posições anteriores */
TipoItem* Retira (Posicao p, TipoLista* Lista) {
  int Aux; 
  TipoItem* item;
  item = (TipoItem*) malloc(sizeof(TipoItem)); 
  if (Vazia(Lista) || p >= Lista->Ultimo){
    cout << "A posição não existe!" << endl;
    return NULL; 
  }
  *item = Lista->Item[p]; 
  Lista->Ultimo--; 
  for (Aux = p; Aux < Lista->Ultimo; Aux++)
    Lista->Item[Aux] = Lista->Item[Aux+1]; 
  return item;
}

/*Imprime os itens da lista na ordem de ocorrência */ 
void Imprime (TipoLista* Lista, bool tipoDeImpressao){
    if (tipoDeImpressao == false){
      cout << "p - key" << endl;
      for (int Aux = Lista->Primeiro; Aux < Lista->Ultimo; Aux++){
        cout << Aux << " - " << Lista->Item[Aux].valor << endl;
      }
    }else{
      cout << "p - Elem - Count" << endl;
      for (int Aux = Lista->Primeiro; Aux < Lista->Ultimo; Aux++){
        cout << Aux << " -   " << Lista->Item[Aux].listaAuxiliar[0] << "  -   " <<Lista->Item[Aux].listaAuxiliar[1]<< endl;
      } 
    }
} 

/*Fornece o maior e o menor elemento mais o número de ocorrências dele */
void MaisEMenosVezes(TipoLista* Lista){
  int maior = 0;
  int menor = 0;
  int ocorrencias = 0;
  int ocorrenciaMenor;
  int ocorrenciaMaior;
  
  for(int Aux = Lista->Primeiro; Aux < Lista->Ultimo; Aux++){
    for(int Aux2 = Lista->Primeiro; Aux2 < Lista->Ultimo; Aux2++){
      if (Lista->Item[Aux2].valor == Lista->Item[Aux].valor){
        ocorrencias++;
      }
    }
    if (Aux == Lista->Primeiro){
      ocorrenciaMaior = ocorrencias;
      maior = Lista->Item[Aux].valor;
      ocorrenciaMenor = ocorrencias;
      menor = Lista->Item[Aux].valor;
    }
    else if (ocorrencias > ocorrenciaMaior){
      ocorrenciaMaior = ocorrencias;
      maior = Lista->Item[Aux].valor;
    }
    else if (ocorrencias <= ocorrenciaMenor){
      ocorrenciaMenor = ocorrencias;
      menor = Lista->Item[Aux].valor;
    }
    ocorrencias = 0;
  }
  if (ocorrenciaMaior == ocorrenciaMenor){
    cout << "Todos os elementos tem a mesma ocorrência";
  } else {
  cout << "elemento com mais ocorrencias : " << maior << " -> " << ocorrenciaMaior << " vez/vezes" << endl;
  cout << "elemento com menos ocorrencias : " << menor << " -> " << ocorrenciaMenor << " vez/vezes" << endl;
  }

}

TipoLista* ListaElemECount(TipoLista* Lista){
  int ocorrencias = 0;
  bool verificadorDeInsercao = true;
  TipoItem* item;
  item = (TipoItem*)malloc(sizeof(TipoItem));
  TipoLista* listaRetornada;
  listaRetornada = InicializaLista();
  for(int Aux = Lista->Primeiro; Aux < Lista->Ultimo; Aux++){
    for(int Aux2 = Lista->Primeiro; Aux2 < Lista->Ultimo; Aux2++){
      if (Lista->Item[Aux2].valor == Lista->Item[Aux].valor){
        ocorrencias++;
      }
    }
    item->listaAuxiliar[0] = Lista->Item[Aux].valor;
    item->listaAuxiliar[1] = ocorrencias; 
    int Aux3 = Lista->Primeiro;
    while (Aux3 <= listaRetornada->Ultimo - 1 && verificadorDeInsercao == true){
      if (listaRetornada->Item[Aux3].listaAuxiliar[0] == Lista->Item[Aux].valor){
        verificadorDeInsercao = false;
      }
      Aux3++;
    } 
    if (verificadorDeInsercao){
      Insere(item, listaRetornada);
    }
    verificadorDeInsercao = true;  
    ocorrencias = 0;
  }
  return listaRetornada;
}