    #include<stdio.h>
    #include<stdlib.h>
    #include<time.h>

    typedef struct node{
        int key;
        struct node* next;
    }node;
    typedef struct node* nodeptr;
    nodeptr createnode(int key){
        nodeptr temp = (nodeptr)malloc(sizeof(node));
        temp->key=key;
        temp->next=NULL;
        return temp;
    }
    int search(nodeptr* hashtable, int val, int m, int* totsucc){
        int ind = val%m;
        nodeptr temp=hashtable[ind];
        while(temp!=NULL){
            (*totsucc)++;
            if(temp->key==val){
                return 1;
            }
            temp=temp->next;
        }
        return 0;
    }
    void hashthatshi(int n, int m){
        nodeptr hashtable[m];
        for(int i=0;i<m;i++){
            hashtable[i]=NULL;
        }
        int vals[n];
        for(int i=0;i<n;i++){
            int k=rand()%1000;
            vals[i]=k;
        }

        for(int i=0;i<n;i++){
            int k=vals[i];
            nodeptr temp=createnode(k);
            int h=k%m;
            temp->next=hashtable[h];
            hashtable[h]=temp;
        }

        int totsucc=0;
        for(int i=0;i<n;i++){
            int k=vals[i];
            search(hashtable, k, m, &totsucc);
        }
        double avgsucc = (double) totsucc/(double) n;
        printf("AVG SUCC=%.2f", avgsucc);

        int totfail=0;
        for(int i=0;i<n;i++){
            int k=rand()%1000+1001;
            search(hashtable, k, m, &totfail);
        }
        double avgfail = (double) totfail/(double)n;
        printf("AVG fail=%.2f", avgfail);

    }

    int main(){
        srand(time(NULL));
        int n=200, m=50;
        hashthatshi(n, m);
        return 0;
    }
