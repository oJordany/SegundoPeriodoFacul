#include <iostream>
#include "funcoes.h"
using namespace std;

// Código principal
int main() {
  // Primeiro teste feito na aula:
  char c = 97;
  cout << " caracter " << c << ", em decimal " << (int) c; // usando o (int) c, ele imprime o valor do codigo numerico
  cout << endl;
  cout << endl;
  
  // Representação de caracteres em C (serve para C++ tb)
  char caracter = 'a';
  cout << " caracter " << c << ", em decimal " << (int) caracter << endl;
  cout << endl;

  // Usando a função que verifica se um caracter é de 0 a 9
  char d = '1';
  if (verificaDigito(d))
    cout << "caracter "<< d << "|" << (int) d <<" é um dígito" << endl;
  else
    cout << "caracter "<< d << "|" << (int) d <<" não é um dígito" << endl;

  // Usando a função que verifica se um caracter é Letra maiuscula ou minuscula
  char v = 'b';
  if (verificaLetra(d))
    cout << "caracter "<< v << "|" << (int) d <<" é uma letra" << endl;
  else
    cout << "caracter "<< v << "|" << (int) d <<" não é uma letra" << endl;
  
  // Usando a função que passa para maiúscula
  cout << "caracter " << c << " em maiúscula " << maiuscula(c) << endl;
  
  // Cadeias de caracteres (string)
  char str[4];
  str[0] = 'o';
  str[1] = 'l';
  str[2] = 'a';
  str[3] = '\0';
  cout << str << endl;

  cout << endl;

  // Outras representações
  char str2[] = "ola"; 
  /* 
    No final das contas, ele tem 4 posições, contando com o vazio \0 . 
    Nesse caso, eu meio que já to definido o tamanho, que é o tamanho da string que eu to passando
  */
  cout << str2 << endl;

  char str3 [] = {'o', 'l', 'a', '\0'};
  cout << str3 << endl;

  // Convertendo uma cadeia de caracteres para string:
  char str4[] = "Rio de Janeiro!";
  int ultimaPosicao;
  int i = 0;
  while (str4[i] != '\0'){
    cout << maiuscula(str4[i]);
    i++;
  }

  cout << endl;
  
  // Vou deixar essa variável space para quando eu quiser dar espaço 
  char space = 32;
  cout << space << space << "n" << endl;

  // Usando cin com especificação do formato char a;
  char a;
  cout << "insira um caracter: ";
  cin >> a;
  cout << "caracter " << a << endl;

  // Usando cin com especificação do formato string;

  char cidade[81];
  cout << "Coloca uma cidade aí: ";
  cin >> cidade;
  cout << "cidade " << cidade << endl;

  /* 
  para capturar nomes compostos:
    cin.get(nome, 100)
      Lê até o 99º caractere ou <ENTER>
      Garante que o tamanho é suficiente
  */
  char nome[81];
  cout << "Insira um nome qualquer: ";
  cin.ignore(); // Usa isso, pq senão dá um bug e ele não pega no cin logo
  cin.get(nome, 81);
  cout << "nome: " << nome << endl; 
  
  return 0;
}
