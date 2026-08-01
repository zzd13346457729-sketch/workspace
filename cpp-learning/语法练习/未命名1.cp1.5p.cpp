#include<stdio.h>
int main(){
	double r,h;
	double pai=3.1415926535;
	scanf("%lf%lf",&r,&h);
	printf("%.3f\n",r*r*pai*2+2*pai*r*h);
	return 0;
}
