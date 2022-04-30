typedef int Posicao;
#define InicioVetor 0
#define MaxTam  1000

typedef struct{
  int valor;
  int listaAuxiliar[2];
}TipoItem;

typedef struct{
  TipoItem Item[MaxTam];
  Posicao Primeiro, Ultimo;
}TipoLista;

TipoLista* InicializaLista();
void FLVazia (TipoLista* Lista);
int Vazia (TipoLista* Lista);
int Tamanho_lista(TipoLista* Lista);
void Insere (TipoItem* x, TipoLista* Lista); 
TipoItem* Busca(int chave, TipoLista* lista);
TipoItem* Retira (Posicao p, TipoLista* Lista); 
void Imprime (TipoLista* Lista, bool tipoDeImpressao=false); 

void MaisEMenosVezes(TipoLista* Lista);
TipoLista* ListaElemECount(TipoLista* Lista);