#include <stdio.h>
int main()
{
    int n;
    scanf("%d",&n);
    for(int i=1;i<=n;i++){///����i
        for(int j=1;j<=n;j++){///�k��i
            printf("*");

        }
        printf("i:%d\n",i);
    }
}
