#include<stdio.h>
#include<stdlib.h>

int mat[100][100];

void warshalls(int graph[100][100], int n){
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            mat[i][j]=graph[i][j];
        }
    }
    
    for(int k=0;k<n;k++){
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                mat[i][j]=mat[i][j] || (mat[i][k] && mat[k][j]);
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
    int n;
    printf("Enter the number of vertices in the graph: ");
    scanf("%d", &n);
    int graph[n][n];
    printf("Enter the adjacency matrix:\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            scanf("%d", &graph[i][j]);
        }
    }

    warshalls(graph, n);

    return 0;
}
