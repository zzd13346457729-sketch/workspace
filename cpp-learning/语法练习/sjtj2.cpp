#include<stdio.h>
#define INF 1000000000
int main(){
	FILE *fin,*fout;
	fin=fopen("sjtj2.in","rb");
	fout=fopen("sjtj2.out","wb");
	int case1=0,n=0,x=0;
	while(fscanf(fin,"%d",&n)!=EOF&&n){
		int s=0,max=-INF,min=INF;
		for(int i=1;i<=n;i++){
			fscanf(fin,"%d",&x);
			if(x>max) max=x;
			if(x<min) min=x;
			s+=x;
		}
		if(case1) fprintf(fout,"\n");
		case1++;
		fprintf(fout,"Case %d: %d %d %.3f\n",case1,max,min,(double)s/n);
	}
	return 0;
}
