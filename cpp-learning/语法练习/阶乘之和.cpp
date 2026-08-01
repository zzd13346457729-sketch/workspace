#include<stdio.h>
#include<time.h>
int main(){
	int n,S=0;
	const int mod=1000000;
	scanf("%d",&n);
	if(n>25) n==25;
	for(int i=1;i<=n;i++){
		int f=1;
		for(int j=1;j<=i;j++){
			f=(f*j)%mod;
		}
		S=(S+f)%mod;
	}
	printf("%d\n",S);
	printf("Time Used =%.2f\n",(double)clock() / CLOCKS_PER_SEC);
	return 0;
} 
