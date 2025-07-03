#include<stdlib.h>
#include<stdio.h>
#include<time.h>

int search(int* hashtable, int m, int key, int* tot){
    int ind=key%m;
    int start=ind;
    while(hashtable[ind]!=-1){
        (*tot)++;
        if(hashtable[ind]==key)return 1;
        ind=(ind+1)%m;
        if(ind==start)return 0;
    }
    return 0;
}

void hashthatshi(int n, int m){
    int hashtable[m];
    for(int i=0;i<m;i++){
        hashtable[i]=-1;
    }

    int vals[n];
    for(int i=0;i<n;i++){
        vals[i]=rand()%1000;
    }

    for(int i=0;i<n;i++){
        int key=vals[i];
        int ind=key%m;
        while(hashtable[ind]!=-1){
            ind=(ind+1)%m;
        }
        hashtable[ind]=key;
    }

    int totsucc=0;
    for(int i=0;i<n;i++){
        search(hashtable, m, vals[i], &totsucc);
    }
    double avgsucc = (double) totsucc/(double) n;
    printf("AVG SUCC=%.2f", avgsucc);

}


int main(){
    srand(time(NULL));
    int n=50, m=100;
    hashthatshi(n, m);
    return 0;
}
