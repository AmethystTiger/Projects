#include<stdio.h>
#include<stdlib.h>

int knapsack(int* weight, int* value, int n, int W){
    int dp[n+1][W+1];
    for(int i=0;i<=n;i++){
        for(int j=0;j<=W;j++){
            if(i==0 || j==0)dp[i][j]=0;
            else if(weight[i-1]<=j){
                int x = dp[i-1][j];
                int y = value[i-1]+dp[i-1][j-weight[i-1]];
                dp[i][j]=x>y?x:y;
            }
            else{
                dp[i][j]=dp[i-1][j];
            }
            printf("%d ", dp[i][j]);
        }
        printf("\n");
    }
    return dp[n][W];

}

int main()
{
    int n = 4;
    int W = 7;
    int weight[] = {1, 3, 4, 5};
    int value[] = {1, 4, 5, 7};    

    printf("Maximum profit: %d\n", knapsack(weight, value, n, W));

    return 0;
}
