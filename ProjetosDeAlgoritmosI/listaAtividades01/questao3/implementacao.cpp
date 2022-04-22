#include <iostream>
#include "funcoes.h"
#include <string.h>

using namespace std;

void localizaCaracteres(char *busca, char *cadeia){
    bool verificador = true;
    int indiceBusca = 0;
    int repeticoes = 0;

    // loop que localiza vai localizando a busca de caractere por caractere
    for (int i = 0; i <= strlen(cadeia) - strlen(busca); i++){
        for(int j = i; j < i+strlen(busca); j++){
            if (cadeia[j] != busca[indiceBusca])
                verificador = false;
            indiceBusca++;
            }
            indiceBusca = 0;

        if(verificador && repeticoes == 0){
            repeticoes++;
            cout << "A cadeia de caracteres \"" << busca << "\" pode ser encontrada no(s) índice(s) " << i << ", ";
        }else if (verificador && repeticoes > 0){
            cout << i << ", ";
            repeticoes++;
        }
        verificador = true;
    }

    // caso a busca não esteja presente nenhuma vez na cadeia de caracteres
    if (repeticoes == 0)
        cout << "não foi possível encontrar a cadeia de caracteres \"" << busca << "\" ";
        
    cout << "na cadeia \"" << cadeia <<"\""<< endl;
}