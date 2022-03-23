#include <iostream>
#include <math.h>
using namespace std;

int main(){
    //01. Escreva um algoritmo que verifica se um número é negativo, positivo ou igual a zero.
    int numero;
    cout << "Escreva um número: ";
    cin >> numero;
    if (numero > 0) {
        cout << "O número é positivo" << endl;
    } else if (numero < 0) {
        cout << "O número é negativo" << endl;
    } else {
        cout << "O número é 0" << endl;
    }


    //02. Escreva um algoritmo que encontre o máximo e o mínimo entre dois números reais.
    int a = 0, b =0;
    cout << "Escreva um valor: ";
    cin >> a;
    cout << "Escreva outro valor: ";
    cin >> b;
    if (a > b){
        cout << a << " é maior que " << b << endl;
    } else if (a < b){
        cout << a << " é menor que " << b << endl;
    } else {
        cout << a << " é igual a " << b << endl;
    }


    //03. Escreva um algoritmo que mostre em orem 3 números inteiros:
    int num1, num2, num3;
    cout << "Digite 3 números inteiros separando-os por espaço: ";
    cin >> num1 >> num2 >> num3;
    if (num1 < num2 && num2 < num3){
        cout << num1 << " - " << num2 << " - " << num3 << endl;
    } else if (num1 > num2 && num2 > num3){
        cout << num3 << " - " << num2 << " - " << num1 << endl;
    } else if (num3 > num1 && num1 > num2){
        cout << num2 << " - " << num1 << " - " << num3 << endl;
    } else if (num2 > num1 && num1 > num3){
        cout << num3 << " - " << num1 << " - " << num2 << endl;
    } else if (num2 > num3 && num3 > num1) {
        cout << num1 << " - " << num3 << " - " << num2 << endl;
    } else {
        cout << "São todos iguais" << endl;
    }
    return 0;
}