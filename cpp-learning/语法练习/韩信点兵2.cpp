#include<stdio.h>
int main(){
	int x,y,z,case1=0;
	while(scanf("%d%d%d",&x,&y,&z)!=EOF){
		int f=0;
		case1++;
		for(int i=10;i<=100;i++){
			if(i%3==x&&i%5==y&&i%7==z){
				f=1;
				printf("Case %d: %d\n",case1,i);
				break;
			}
		} 
		if(f==0) printf("Case %d: No answer\n",case1);
	}
	return 0;
}
