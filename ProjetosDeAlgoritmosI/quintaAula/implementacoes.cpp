#include <iostream>
#include "funcoes.h"

using namespace std;

int verificaDigito(char c) {
  if ((c >= '0') && (c <= '9'))
    return 1;
  else
    return 0;
}

int verificaLetra(char c) {
  if ((c >= 'a') && (c <= 'z') || (c >= 'A') && (c <= 'Z'))
    return 1;
  else
    return 0;
}

char maiuscula(char c) {
  if (c>='a' && c <='z')
    c = c - 'a' + 'A';
  return c;
}