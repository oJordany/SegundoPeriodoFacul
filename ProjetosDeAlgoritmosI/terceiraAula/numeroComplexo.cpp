#include <iostream>
#include "numeroComplexo.h"

using namespace std;

numeroComplexo inicializa(int real, int imaginario){
    numeroComplexo numero;
    numero.real = real;
    numero.imaginaria = imaginario;
    return numero;
}

void imprime(numeroComplexo numero){
    cout << "real " << numero.real << " imaginario " << numero.imaginaria << "\n";
}

void copia(numeroComplexo *numero, numeroComplexo copia){
    (*numero).real = copia.real;
    (*numero).imaginaria = copia.imaginaria;
}

numeroComplexo soma(numeroComplexo num1, numeroComplexo num2){
    num1.real = num1.real + num2.real;
    num1.imaginaria = num1.imaginaria + num2.imaginaria;
    return num1;
}

int ehReal(numeroComplexo num){
    if (num.imaginaria == 0){
        return 0;
    }else{
        return 1;
    }
}