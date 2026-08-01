#include<stdio.h>
int main(){
	double sum=0;
	int n=0;
	do{
		if(n%2==0) sum+=1.0/(2*n+1);
		else sum-=1.0/(2*n+1);
		n++;
	}while(2*n+1>=1e-6);
	printf("%.6f\n",sum);
	return 0;
}
