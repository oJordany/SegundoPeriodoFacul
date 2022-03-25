// Primeiro programa feito na aula2
#include <iostream>
using namespace std;
int main() {
  int a = 0;
  while(a < 5){
    cout << a << endl;
    a++;
  }
  cout << endl;
  int i = 100;
  while (i >= -100){
    if (i == -100){
      cout << i << endl;    
    } else{
      cout << i << " ; ";
    }
    i--;
  }
  cout << endl;

  
  //Segundo programa feito na aula2:
  for (int i = 0; i < 5; i++){
    cout << 2*i << endl;
  }
  
  cout << endl;

  for (int cont = 50; cont >= -50; cont--){
    if (cont%2 != 0){
      cout << cont << endl;
    }
  }

  cout << endl;


  //Terceiro programa feito na aula - Detecta se é primo ou não
  int numeroEntrada;
  int divisores = 0;
  cin >> numeroEntrada;
  for (int i = 1; i <= numeroEntrada; i++){
    if (numeroEntrada%i == 0){
      divisores++;
    }
  }
  if(divisores == 2){
    cout << "é primo" << endl;
  } else {
    cout << "não é primo, pois ele é divisível por " << divisores << " numeros, sendo eles: " << endl; 
    for (int k = 1; k <= numeroEntrada; k++){
      if (numeroEntrada%k == 0){
        cout << k << " ";
      }
    }
  }


  cout << endl; 

  // Quarto programa feito na aula - exponenciação com for
  int base, expoente, resultado;
  cin >> base >> expoente;
  resultado = base;
  for (int i = 1; i < expoente; i++){
    resultado = resultado * base;
  }
  cout << base << "^" << expoente << " = " << resultado << endl;


  // Quinto programa feito na aula - Soma de todos os primos entre 1 e 100
  int soma = 0;
  int qtdDeDivisores;
  for (int c = 2; c <= 100; c++){
    qtdDeDivisores = 0;
    for (int i = 1; i <= c; i++){
      if (c%i == 0){
        qtdDeDivisores++;
      }
    }
    if(qtdDeDivisores == 2){
      soma += c;
      if (c == 97){
        cout << c;
      } else {
        cout << c << "+";
      }
    }
  }
  cout << " = "<< soma << endl;


  // Sexto programa feito na aula - O mesmo que no Quarto programa, mas somando
  int b, exp, result, aux;
  cin >> b >> exp;
  result = b;
  aux = b;
  for (int i = 1; i < exp; i++){
    for (int c = 1; c < b; c++){
      result += aux;
    }
    aux = result;
  }
  cout << b << "^" << exp << " = " << result << endl;
}