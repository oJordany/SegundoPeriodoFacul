#include <iostream>
#include "funcoes.h"
using namespace std;

int main() {
  char palavra[81];
  char letra;
  int posicao;
  cout << "Insira uma palavra: ";
  cin.get(palavra, 81);
  cout << "Insira a letra que vc deseja inserir na palavra: ";
  cin >> letra;
  cout << "Insira a posicao da palavra que vc deseja inserir a letra (a primeira posicao inicia em 0): ";
  cin >> posicao;
  trocaLetra(letra, palavra, posicao);
  cout << "A palavra foi transformada: " << palavra << endl;
  return 0;
}