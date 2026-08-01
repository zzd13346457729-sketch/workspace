#include<stdio.h>
int main(){
	int n;
	for(int i=1;i<=9;i++){
		for(int j=0;j<=9;j++){
			for(int k=0;k<=9;k++){
				n=i*i*i+j*j*j+k*k*k;
				if(99<n&&n<1000&&n==i*100+j*10+k) printf("%d\n",n);
			}
		}
	}
}
