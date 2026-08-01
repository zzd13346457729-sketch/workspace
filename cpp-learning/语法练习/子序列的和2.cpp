#include<stdio.h>
#include<math.h>
int main(){
	int n,m,case1=0;
	while(scanf("%d%d",&n,&m)!=EOF&&n&&m){
		double s=0.0;
		for(int i=n;i<=m;i++){
			s+=1.0/i/i;
		}
		case1++;
		printf("Case %d: %.5f\n",case1,s);
	}
	return 0;
}
