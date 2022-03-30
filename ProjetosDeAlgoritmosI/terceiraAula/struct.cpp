#include <iostream>
#include <string>

using namespace std;

struct aluno {
    int matricula;
    char conceito;
    string nome;
};

int main(void){
    struct aluno al, aux;
    al.nome = "Pedro";
    al.matricula = 200712;
    al.conceito = 'a';
    aux = al;
    cout << al.nome << " " << al.matricula << " " << al.conceito << endl;
    cout << aux.nome << " " << aux.matricula << " " << aux.conceito << endl;
    return 0;
}