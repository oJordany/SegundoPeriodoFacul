#include <iostream>
#include "funcoes.h"
#include <string.h>

using namespace std;

int contaVogais(char *palavra) {
  int numeroVogais = 0;
  int i = 0;
  while (i != strlen(palavra)){
    if (palavra[i] == 'a' || palavra[i] == 'e' || palavra[i] == 'i' || palavra[i] == 'o' || palavra[i] == 'u'){
      numeroVogais++;
    }
    i++;
  }
  return numeroVogais;
}