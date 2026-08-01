#include<stdio.h>
int main(){
	int n;
	scanf("%d",&n);
	for(int x=n;x>=1;x--){
		for(int k=1;k<=n-x;k++){
			printf(" ");
		}
		for(int j=1;j<=2*x-1;j++){
			printf("#"); 
		}
		printf("\n"); 
	}
	return 0;
}
