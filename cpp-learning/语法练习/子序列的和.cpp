#include<stdio.h>
int main(){
	int n,m,casen=1;
	while(scanf("%d%d",&n,&m)!=EOF){
		if(n==0&m==0) break;
		double s=0.0;
		for(int i=n;i<=m;i++){
			s+=1.0/i/i;
		}
		printf("Case %d: %.5f\n",casen,s);
		casen++;
	}
	return 0;
} 
