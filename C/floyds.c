#include<stdio.h>
#include<stdlib.h>
#define INF 99999

int mat[100][100];

void floyd(int graph[100][100], int n){
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            mat[i][j]=graph[i][j];
        }
    }
    
    for(int k=0;k<n;k++){
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                int prev = mat[i][j];
                int sum = (mat[i][k] + mat[k][j]);
                mat[i][j]= prev<sum?prev:sum;
            }
        }
    }

    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            printf("%d ", mat[i][j]);
        }
        printf("\n");
    }

}

int main()
{
    int n=5;
    /*
    printf("Enter the number of vertices in the graph: ");
    scanf("%d", &n);
    int graph[n][n];

    printf("Enter the adjacency matrix (use %d for infinity):\n", INF);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            scanf("%d", &graph[i][j]);
            if (graph[i][j] == 0 && i != j) {
                graph[i][j] = INF;
            }
        }
    }
    */
   int graph[100][100] = {
    {0,    3, INF,   7, INF},
    {8,    0,   2, INF, INF},
    {5,  INF,   0,   1, INF},
    {2,  INF, INF,   0,   1},
    {INF, INF,   3, INF,   0}
    };
    floyd(graph, n);

    return 0;
}
