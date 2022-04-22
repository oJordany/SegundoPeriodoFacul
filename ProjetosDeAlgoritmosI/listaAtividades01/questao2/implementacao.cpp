#include <iostream>
#include "funcoes.h"
using namespace std;

void trocaLetra(char letra, char *palavra, int posicao) {
  palavra[posicao] = letra;
}