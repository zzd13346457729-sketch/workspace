#include<stdio.h>
#include<math.h>
int main(){
	int a,b,c;
	scanf("%d%d%d",&a,&b,&c);
	if(a*a==b*b+c*c) printf("yes");
	else if(b*b==a*a+c*c) printf("yes");
	else if(c*c==a*a+b*b) printf("yes");
	else printf("not a triangle");
	return 0;
}
