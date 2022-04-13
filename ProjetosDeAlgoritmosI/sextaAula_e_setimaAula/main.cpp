#include <iostream>
#include <string.h>
#include <string>
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


  // Usando a nossa Função compara()
  // E usando a função strcmp()
  cout << endl;
  char word1[81];
  char word2[81];
  cout << "##### Teste usando a nossa função compara() e a strcmp() #####" << endl;
  cout << "Insira a primeira palavra a ser comparada: ";
  cin.ignore();
  cin.get(word1, 81);
  cout << "Insira a segunda palavra a ser comparada: ";
  cin.ignore();
  cin.get(word2, 81);
  compara(word1, word2);
  cout << "Com a nossa função compara() → "<<compara(word1, word2) << endl;
  cout << "Com a função strcmp() → "<<strcmp(word1, word2) << endl;


  // Usando a nossa funcao palíndromo
  // Detecta se uma palavra é palíndromo
  cout << endl;
  char palavra[81];
  cout << "##### Teste usando a nossa função palindromo() #####" << endl;
  cout << "Insira uma palavra para verificar se eh palindromo: " << endl;
  cin.ignore();
  cin.get(palavra, 81);
  cout << palindromo(palavra) << endl;
  return 0;
}
