#include <stdio.h>
#include <stdlib.h>

void heapifybottomup(int* arr, int n){
    int i, j, k, v;
    for(i=(n/2)-1;i>=0;i--){
        k=i;
        v=arr[i];
        while(2*k+1<n){
            j=2*k+1;
            if(j+1<n && arr[j+1]>arr[j]){
                j=j+1;
            }
            if(arr[k]>=arr[j]){
                break;
            }
            else{
                arr[k]=arr[j];
                arr[j]=v;
                k=j;
            }
        }
    }
}

int* heapifytopdown(int* arr, int n){
    int* sol = (int*)calloc(n, sizeof(int));
    for(int i=0;i<n;i++){
        sol[i]=arr[i];
        int j =i;
        while(j>0 && sol[j]>sol[j/2]){
            int temp=sol[j];
            sol[j]=sol[j/2];
            sol[j/2]=temp;
            j=j/2;
        }
    }
    return sol;
}

int* heapsort(int* arr, int n){
    int* sol = (int*)calloc(n, sizeof(int));
    int i=0;
    heapifybottomup(arr, n);
    while(n>0){
        int max=arr[0];
        sol[n-1]=max;
        arr[0]=arr[--n];
        heapifybottomup(arr, n);
    }
    return sol;
}

int main()
{
    int arr[7] = {1, 2, 3, 4, 5, 6, 7};
    int* sol = heapsort(arr, 7);
    for(int i=0;i<7;i++){
        printf("%d ", sol[i]);
    }
    return 0;
}

