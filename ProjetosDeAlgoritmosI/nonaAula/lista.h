//typedef int TipoChave;

typedef struct  {
  int Chave;
  /* outros componentes */
}TipoItem;

// Aqui eu to definindo um novo tipo Apontador que na vdd é um struct Celula_str
// E esse Apontador na vdd é um ponteiro
typedef struct Celula_str* Apontador;
// Aqui eu posso chamar de novo a minha struct Celula_str, que na vdd é um ponteiro 
// Daí eu defino os "atributos" dessa struct
typedef struct Celula_str{
  TipoItem Item;
  Apontador Prox; // Quando eu to chamando o Apontador, na vdd eu to chamando um struct Celula_str*, ou seja, um ponteiro que deverá apontar pra uma struct Celula_str
} Celula; // Aqui eu to definindo o tipo Celula pra não precisar chamar toda vez struct Celula_str quando eu for criar uma Celula

typedef struct{
  Apontador Primeiro, Ultimo;
} TipoLista;

TipoLista* InicializaLista();
void FLVazia (TipoLista* ); 
int Vazia (TipoLista *);
void Insere (TipoItem , TipoLista *, Apontador); 
TipoItem RetiraIni (Celula*, TipoLista *);
TipoItem RetiraFinal (Celula*, TipoLista *);
void Imprime (TipoLista* );
int Tamanho_lista(TipoLista* );
int Busca(int , TipoLista* );

//TODO: funções a serem implementadas
TipoItem* InicializaTipoItem();
void ModificaValorItem (TipoItem*, int ); 
void ImprimeTipoItem(TipoItem* );