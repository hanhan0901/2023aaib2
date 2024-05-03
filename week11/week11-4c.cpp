#include <stdio.h>
int main()
{
	int a[10][10];
	int m,n;///part 1 :input
	scanf("%d%d",&m,&n);
	for(int i=0;i<m;i++){
		for(int j=0;j<n;j++){
		scanf("%d",&a[i][j]);
		}
	}
	///part 2: Output
	printf("\n");
	for(int j=0;j<n;j++){///part3
		for(int i=m-1;i>=0;i--){///part
			printf("%2d ",a[i][j]);
		}
		printf("\n");
	}

}
