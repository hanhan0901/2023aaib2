///week11-2.cpp篩子法
///以前的寫法,要30萬*30萬=900億次
///用篩子法,只要30萬+殺掉的那些格子,快20萬倍
#include <stdio.h>
int main()
{
    int BOUND = 300000,ans=0;
    int table[300000] = {};
    for(int i=2;i<BOUND;i++){
        if(table[i]==0){
            ans++;
            for(int k=i;k<BOUND;k+=i){
                table[k] = -1;///殺死它
            }
        }
    }
    printf("質數有:%d 個\n",ans);
}
