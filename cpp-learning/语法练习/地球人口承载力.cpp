#include<cstdio>
using namespace std;
int main(){
	int x,a,y,b,s1,s2;
	float n;
	scanf("%d %d %d %d",&x,&a,&y,&b);
	s1=a*x;
	s2=b*y;
	n=(s2-s1)/(b-a);
	printf("%0.2f",n);
	return 0;
}
