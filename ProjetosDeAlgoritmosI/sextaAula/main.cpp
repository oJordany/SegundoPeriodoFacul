#include <iostream>
#include <string>
#include <string.h>
#include "funcoes.h"

using namespace std;

int main() {
  // A função getline() é capaz de ler o dado de entrada até que uma nova linha seja detectada
  string city;
  char c[81];
  char origem[81];
  char destino[81];
  char palavra1[81];
  char palavra2[81];
  
  // Uando o getline:
  cout << "Digite uma cidade: ";
  getline(cin, city);
  cout << "cidade: " << city << endl;

  
  // Usando a nossa funcao comprimento()
  // E usando a função strlen()
  cout << endl << "Digite uma palavra: ";
  cin.ignore();
  cin.get(c, 81);
  cout << "com comprimento() → " <<comprimento(c) << endl;
  cout << "com strlen() → "<<strlen(c) << endl;


  // Usando a nossa função copia()
  // E usando a função 
  cout << endl <<"#### Teste Usando A nossa função copia() ####" << endl;
  cout << "insira a palavra que será copiada (origem): ";
  cin.ignore();
  cin.get(origem, 81);
  copia(destino, origem);
  cout << "A palavra foi copiada e colada em destino[81]" << endl;
  cout << "origem: " << origem <<  " | destino: " << destino << endl;
  cout << "#### Teste usando a função strcpy() ####" << endl;
  cout << "insira a palavra que será copiada (origem): ";
  cin.ignore();
  cin.get(origem, 81);
  strcpy(destino, origem);
  cout << "A palavra foi copiada e colada em destino[81]" << endl;
  cout << "origem: " << origem <<  " | destino: " << destino << endl << endl;


  // Usando a nossa Função concatena()
  // E usando a função strcat()
  cout << "##### Teste usando a nossa função concatena() #####" << endl;
  cout << "Insira a palavra1: ";
  cin.ignore();
  cin.get(palavra1, 81);
  cout << "Insira a palavra2: ";
  cin.ignore();
  cin.get(palavra2, 81);
  concatena(palavra1, palavra2);
  cout << "a palavra2 foi concatenada com a palavra1" << endl;
  cout << "Palavra concatenada (palavra1): " << palavra1 << endl;
  cout << "##### Teste usando a nossa função strcat() #####" << endl;
  cout << "Insira a palavra1: ";
  cin.ignore();
  cin.get(palavra1, 81);
  cout << "Insira a palavra2: ";
  cin.ignore();
  cin.get(palavra2, 81);
  strcat(palavra1, palavra2);
  cout << "a palavra2 foi concatenada com a palavra1" << endl;
  cout << "Palavra concatenada (palavra1): " << palavra1 << endl;
  
  return 0;
}