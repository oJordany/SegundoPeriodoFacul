#include <iostream>
#include <string>
#include <math.h>
using namespace std;

int main(){
    // Primeira parte da aula:
    cout << "Hello World!!!" << endl;


    //Segunda parte da aula:
    //Palavras Reservadas
    //Variáveis e tipos de dados
    //Tamanho dos tipos de dados
    cout << "Size of char: " << sizeof(char) << endl;
    cout << "Size of int: " << sizeof(int) << endl;
    cout << "Size of short int: " << sizeof(short int) << endl;
    cout << "Size of long int: " << sizeof(long int) << endl;
    cout << "Size of float: " << sizeof(float) << endl;
    cout << "Size of double: " << sizeof(double) << endl;
    cout << "Size of wchar_t: " << sizeof(wchar_t) << endl;

    
    //Terceira parte da aula:
    //Criação de variáveis
    int inteiro;
    double comParteFracionariaGrande;
    bool booleano;
    char caractere;
    float comParteFracionariaPequena;
    //Inicialização de variáveis
    inteiro = 10;
    comParteFracionariaGrande = 10.9999;
    caractere = 'a';
    booleano = true;
    comParteFracionariaPequena = 10.99;
    cout << inteiro << comParteFracionariaGrande << booleano << caractere << comParteFracionariaPequena << endl;


    //Quarta parte da aula:
    //Saída Básica
    int num = 10;
    cout << "valor = " << num << " | ";
    cout << "valor = " << num << endl;
    //Entrada básica
    cin >> num;
    cout << "valor = " << num << endl;
    //Entrada de string com espaço
    string name = "Escreva o nome completo: ";
    cout << name << endl;

    getline(cin, name);

    cout << name << endl;


    // Quinta Parte da Aula:
    // Operações aritméticas básicas
    int a = 16, b = 4;

    cout << a+b << endl;
    cout << a-b << endl;
    cout << a*b << endl;
    cout << a/b << endl;
    cout << pow(a,2) << endl;
    cout << sqrt(a) << endl;

    //Sexta Parte da Aula:
    float nota1, nota2;
    cin >> nota1 >> nota2;
    cout << "A média das suas notas é " << (nota1+nota2)/2 << endl;


    //Sétima Parte da Aula:
    // Estrutura de decisão if/else
    bool comprar;
    double preco, dinheiro;

    dinheiro = 200;
    preco = 150;
    comprar = (dinheiro >= preco);
    if (comprar){
        cout << "Você tem dinheiro suficiente. Compre!" << endl;
    } else {
        cout << "Você está duro! Sem chance!" << endl;
    }
    return 0;
}
