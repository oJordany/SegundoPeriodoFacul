#include <iostream>
#include "funcoes.h"

using namespace std;

int comprimento(char *c){
  int n = 0;
  while(c[n] != '\0'){
    n++;
  }
  return n;
}


void copia(char *destino, char *origem){
  int i = 0;
  while (origem[i] != '\0'){
    destino[i] = origem[i];
    i++;
  }
  destino[i] = '\0';
}


void concatena(char *destino, char *origem){
  int indiceDeDestino = 0;
  int indiceDeOrigem;
  while (destino[indiceDeDestino] != '\0'){ // Acha o final de destino
    indiceDeDestino++;
  }
  for (indiceDeOrigem=0; destino[indiceDeOrigem] != '\0'; indiceDeOrigem++){
      destino[indiceDeDestino] = origem[indiceDeOrigem];
    indiceDeDestino++;
  }
  destino[indiceDeDestino] = '\0';
}