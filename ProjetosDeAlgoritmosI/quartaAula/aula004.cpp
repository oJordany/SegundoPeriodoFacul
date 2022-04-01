#include <iostream>

using namespace std;

int main(int argc, char** argv) {
    int a = 10;
    int* b;

    b = &a;


    cout << "conteudo de a : "<< a << endl;

    (*b) = 20;
    
    cout << "endereco de b : "<< b << endl;

    cout << "conteudo de a : "<< a << endl;


    return 0;
}