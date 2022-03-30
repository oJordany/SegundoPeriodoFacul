#include <iostream>
#include "numeroComplexo.h"

using namespace std;

int main() {
    numeroComplexo a, b, c, d;
    a = inicializa(2,5);
    cout << "a = ";
    imprime(a);
    b = inicializa(1,2);
    cout << "b= ";
    imprime(b);
    c = soma(a, b);
    cout << "c= ";
    imprime(c);
    d = inicializa(5,0);
    cout << "d= ";
    imprime(d);
    if (ehReal(d) == 0){
        copia(&d, a);
    }
    cout << "d= ";
    imprime(d);
}