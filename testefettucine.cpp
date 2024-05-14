#include <stdio.h>

int main(){
	int x, y, posi, termo;
	
	printf("Digite um Numero: ");
	scanf("%d", &x);
	
	printf("Digite outro Numero: ");
	scanf("%d", &y);
	
	for(posi=3;posi<=10;posi++)
	{
		int termo = y;
		if(posi%2 == 0) 
			y= y - x;
		else 
			y= y + x;
		x=termo;
		printf("\n%d\n", y);
	}
}
