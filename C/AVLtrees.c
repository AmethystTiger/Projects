#include <stdio.h>
#include <stdlib.h>

typedef struct node{
    int key;
    struct node *lchild, *rchild;
}node;
typedef struct node* nodeptr;
nodeptr createnode(int key, nodeptr l, nodeptr r){
    nodeptr temp = (nodeptr)malloc(sizeof(node));
    temp->key=key;
    temp->lchild=l;
    temp->rchild=r;
    return temp;
}

int calcheight(nodeptr root){
    if(root==NULL){
        return 0;
    }
    int right = calcheight(root->rchild);
    int left = calcheight(root->lchild);
    return (right>left?right:left)+1;
}
int balancefactor(nodeptr root){
    return calcheight(root->lchild)-calcheight(root->rchild);
}

nodeptr leftrotate(nodeptr root){
    nodeptr temp = root->rchild;
    root->rchild=temp->lchild;
    temp->lchild=root;
    return temp;
}
nodeptr rightrotate(nodeptr root){
    nodeptr temp = root->lchild;
    root->lchild=temp->rchild;
    temp->rchild=root;
    return temp;
}
nodeptr createAVL(nodeptr root, int val){
    if(root==NULL){
        return createnode(val, NULL, NULL);
    }
    if(val<root->key){
        root->lchild=createAVL(root->lchild, val);
    }
    else if(val>root->key){
        root->rchild=createAVL(root->rchild, val);
    }
    else{
        printf("Duplicate value");
        exit(0);
    }

    int bfac = balancefactor(root);
    if(bfac>1 && val<root->lchild->key){
        return rightrotate(root);
    }
    if(bfac>1 && val>root->lchild->key){
        root->lchild=leftrotate(root->lchild);
        return rightrotate(root);
    }

    if(bfac<-1 && val>root->rchild->key){
        return leftrotate(root);
    }
    if(bfac<-1 && val<root->rchild->key){
        root->rchild=rightrotate(root->rchild);
        return leftrotate(root);
    }
    return root;
}

void succandpred(nodeptr root, int key){
    while(root!=NULL){
        if(key<root->key){
            root=root->lchild;
        }
        else if(key>root->key){
            root=root->rchild;
        }
        else{
            nodeptr pred=root->lchild;
            if(pred!=NULL){
                while(pred->rchild!=NULL){
                    pred=pred->rchild;
                }
                printf("Predecessor: %d", pred->key);
            }
            else printf("No predecessor");

            nodeptr succ=root->rchild;
            if(succ!=NULL){
                while(succ->lchild!=NULL){
                    succ=succ->lchild;
                }
                printf("\nSuccessor: %d", succ->key);
            }
            else printf("\nNo successor");
            return;
        }
    }
    printf("Key not found");
}
/*
nodeptr createBST(nodeptr root, int val){
    if(root==NULL){
        return createnode(val, NULL, NULL);
    }
    if(val<root->key){
        root->lchild=createBST(root->lchild, val);
    }
    else if(val>root->key){
        root->rchild=createBST(root->rchild, val);
    }
    else{
        printf("Duplicate value");
        exit(0);
    }
    return root;
}
*/
void inorder(nodeptr root){
    if(root!=NULL){
        inorder(root->lchild);
        printf(" %d ",root->key);
        inorder(root->rchild);
    }
}
void preorder(nodeptr root){
    if(root!=NULL){
        printf(" %d ",root->key);
        preorder(root->lchild);
        preorder(root->rchild);
    }
}
void postorder(nodeptr root){
    if(root!=NULL){
        postorder(root->lchild);
        postorder(root->rchild);
        printf(" %d ",root->key);
    }
}
void main(){
    int n,x,ch,i;
    nodeptr root;
    root=NULL;

    while(1){
        printf("********************Output********************\n\n");
        printf("-----------Menu-----------\n");
        printf(" 1. Insert\n 2. All traversals\n 3. Exit\n");
        printf("Enter your choice:");
        scanf("%d",&ch);
        switch(ch){
            case 1: 
                printf("Enter node (do not enter duplicate nodes):\n");
                scanf("%d",&x);
                root=createBST(root,x);
                break;
            case 2: 
                printf("\nInorder traversal:\n");
                inorder(root);
                printf("\nPreorder traversal:\n");
                preorder(root);
                printf("\nPostorder traversal:\n");
                postorder(root);
                printf("\n\n*********************************************");
                break;
            case 3: 
                exit(0);
        }
    }
}