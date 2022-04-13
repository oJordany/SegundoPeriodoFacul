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

int compara(char *s1, char *s2){
  int i;
  for (i = 0; s1[i] != '\0' && s2[i] != '\0'; i++){
    if (s1[i] < s2[i]){
      return -1;
    }
    if (s1[i] > s2[i]){
      return 1;
    }
  }
  if (s1[i] == s2[i])
    return 0;
  else if (s2[i] != '\0')
    return -1;
  else 
    return 1;
}

int palindromo(char *s1){
  char copias1[81];
  copia(copias1, s1);
  concatena(copias1, s1);
  int tamanho = comprimento(copias1);
  for (int i = 0; i != tamanho/2; i++){
    if (s1[i] != copias1[tamanho-(i+1)]){
      return 0;
    }
  }
  return 1;
}