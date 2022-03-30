typedef struct {
    int real;
    int imaginaria;
} numeroComplexo;

numeroComplexo inicializa(int, int);
void imprime(numeroComplexo);
void copia(numeroComplexo*, numeroComplexo);
void soma(numeroComplexo);
numeroComplexo soma(numeroComplexo, numeroComplexo);
int ehReal(numeroComplexo);