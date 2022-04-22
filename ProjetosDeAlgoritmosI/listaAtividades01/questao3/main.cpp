#include <iostream>
#include <string.h>
#include "funcoes.h"

using namespace std;

int main() {
  char caracteres[81];
  char cadeia[81];

  cout << "insira uma cadeia de caracteres: "; 
  cin.get(cadeia, 81);
  cout << "insira outra cadeia: ";
  cin.ignore();
  cin.get(caracteres, 81);

  localizaCaracteres(caracteres, cadeia);
  return 0;
}