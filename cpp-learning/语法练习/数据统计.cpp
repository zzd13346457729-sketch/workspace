#include<stdio.h>
int main(){
	int x,max=0,s=0,min=1000;
	double n=0.0;
	while(scanf("%d",&x)!=EOF){
		n++;
		s+=x;
		if(x>max) max=x;
		if(x<min) min=x;
	}
	printf("%d %d %.3f\n",min,max,double(s/n));
	return 0;
} 
