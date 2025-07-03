#include<stdio.h>
#include<stdlib.h>

int weight[] = {1, 3, 4, 5};
int value[] = {1, 4, 5, 7};    
int f[100][100];

int knapsack(int i, int j){
    int val;
    if(f[i][j]<0){
        if(j<weight[i-1]){
            val=knapsack(i-1, j);
        }
        else{
            int without = knapsack(i - 1, j);
            int with = value[i-1] + knapsack(i - 1, j - weight[i-1]);
            val = (without > with) ? without : with; 
        }
        f[i][j]=val;
    }
    return f[i][j];
}

int main()
{
    int n = 4;
    int W = 7;
    
    for(int i=0;i<=n;i++){
        for(int j=0;j<=W;j++){
            if(j==0 || i==0) f[i][j]=0;
            else f[i][j]=-1;
        }
    }

    printf("Maximum profit: %d\n", knapsack(n, W));
    return 0;
}
