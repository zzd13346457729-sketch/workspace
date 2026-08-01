#include<stdio.h>
#include<limits.h>
int main(){
	int a;
	while(a+1>a){
		a++;
	}
	printf("%d %d\n",a,INT_MAX);
}  

