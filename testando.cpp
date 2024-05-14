#include <stdio.h>

int main(){
int i, qtde, anterior, atual, proximo;

	printf("\nQuantos numeros quer mostrar? ");
	scanf("%d", &qtde);
	printf("\nInforme os dois primeiros termos: ");
	scanf("%d %d", &anterior, &atual);
	printf("\n\nSerie de Fettuccine\n");

	printf("[%d] [%d] ", anterior, atual);
	for(i=3; i if(i % 2 == 0){
		proximo = (atual - anterior);
		}else{
			proximo = (atual + anterior);
		}
		printf("[%d] ", proximo);
		anterior = atual;
		atual = proximo;
	}
return 0;
}
