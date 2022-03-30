#include <iostream>
#include <string>
#include "contaBancaria.h"

using namespace std;

int main(){
    contaBancaria conta;
    conta = inicializa(11, 100);
    cout << "antes da movimentação " << "\n";
    imprime(conta);

    deposito(&conta, 50);

    imprime(conta);

    saque(&conta, 100);

    cout << "depois da movimentação " << "\n";
    imprime(conta);
}

