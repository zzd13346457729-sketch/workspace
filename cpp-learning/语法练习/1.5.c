#include<stdio.h>
int main(){
	double n,s;
	scanf("%lf",&n);
	if(95*n>=300) {s=0.85*95*n;printf("%.3f\n",s);
	}
	else {s=95*n;printf("%.3f\n",s);
	}
	return 0;
} 
