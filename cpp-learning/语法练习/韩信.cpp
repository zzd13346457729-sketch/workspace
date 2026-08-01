#include<stdio.h>
int main(){
	int a,b,c,casen=1;
	while(scanf("%d%d%d",&a,&b,&c)!=EOF){
		int f=0; 
		for(int i=10;i<=100;i++){
			if(i%3==a&&i%5==b&&i%7==c) {
			printf("Case %d: %d\n",casen,i);f=1;break;}
		}
		if(f==0) printf("Case %d: No answer\n",casen);
		casen++;
	}
	return 0;
} 
