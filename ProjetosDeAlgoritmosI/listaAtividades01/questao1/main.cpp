#include <iostream>
#include "funcoes.h"
#include <string.h>

using namespace std;

int main(){
  char palavra[81];
  cout << "Insira uma palavra: ";
  cin.get(palavra, 81);
  cout << "Há " << contaVogais(palavra) << " vogal/vogais nessa palavra." << endl;
  return 0;
}
