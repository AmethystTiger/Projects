#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int* shifttable(int* shift, char* p){
    int m = strlen(p);
    for(int i=0;i<256;i++){
        shift[i]=m;
    }
    for(int i=0;i<m-1;i++){
        shift[(unsigned char)p[i]]=m-1-i;
    }
}

int horspool(char* t, char* p){
    int shift[256];
    shifttable(shift, p);
    int m = strlen(p);
    int n = strlen(t);
    int i=m-1;
    while(i<=n){
        int k=0;
        while(k<m && p[m-1-k]==t[i-k]){
            k++;
        }
        if(k==m){
            return i-k+1;
        }
        else{
            i+=shift[t[i]];
        }
    }
    return -1;
    
}

int main(){
    char t[] = "faieufiaefjao";
    char p[] = "euf";
    int j = horspool(t, p);
    printf("%d ", j);
    return 0;
}

