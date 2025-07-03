#include<stdio.h>
#include<stdlib.h>

int* comparisoncount(int* arr, int n){
    int* ind = (int*)calloc(n, sizeof(int));
    int* sol = (int*)calloc(n, sizeof(int));
    for(int i=0;i<n;i++)ind[i]=0;
    for(int i=0;i<n-1;i++){
        for(int j=i+1;j<n;j++){
            if(arr[i]>arr[j]){
                ind[i]++;
            }
            else ind[j]++;
        }
    }
    for(int i=0;i<n;i++)sol[ind[i]]=arr[i];
    return sol;
}

int* distributioncount(int* arr, int n, int l, int u){
    int* ind = (int*)calloc(n, sizeof(int));
    int* sol = (int*)calloc(n, sizeof(int)); 
    for(int i=0;i<u-l+1;i++)ind[i]=0;
    for(int i=0;i<n;i++)ind[arr[i]-l]++;
    for(int i=1;i<n;i++)ind[i]=ind[i-1]+ind[i];
    for(int i=n-1;i>=0;i--){
        int j=arr[i]-l;
        sol[ind[j]-- -1]=arr[i];
    }
    return sol;
}

int main(){
    int arr[10]={1, 1, 1, 2, 1, 2, 2, 3, 3, 3};
    int* b = distributioncount(arr, 10, 1, 3);
    for(int i=0; i<10;i++){
        printf("%d ", b[i]);
    }
    return 0;
}
