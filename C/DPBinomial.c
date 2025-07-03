#include <stdio.h>
#include <stdlib.h>

int c[100][100];

void binomial(int n, int k){
    for(int i=0;i<=n;i++){
        for(int j=0;j<=(i<k?i:k);j++){
            if(j==0 || j==i){
                c[i][j]=1;
            }
            else{
                c[i][j]=c[i-1][j-1]+c[i-1][j];
            }
        }
    }
}

int main()
{
    int n=6, k=3;
    binomial(n, k);
    for(int i=0;i<=n;i++){
        for(int j=0;j<=(i<k?i:k);j++){
            printf("%d ", c[i][j]);
        }
        printf("\n");
    }
    return 0;
}

