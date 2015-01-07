#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{

    typedef struct node
    {
        char word[10];
        struct node* next;
    }
    node;
    int index = 0;
    node* dict[3];
    node* tmp;
      
    dict[index]= malloc(sizeof(node));
    strcpy(dict[index]->word,"cat");
    dict[index]->next = NULL;
    
    tmp = dict[index];
    dict[index]= malloc(sizeof(node));
    strcpy(dict[index]->word,"dog");
    dict[index]->next = tmp;
   
    printf("Dict: %s\n", dict[index]->word);
    
    printf("\nTraversing the linked list node by node...\n");
    
    node* cursor = dict[index]; //add a node pointer that can traverse the linked list
    int count = 1;
    while (cursor != 0)
    {
        printf("Word #%d is: %s\n", count, cursor->word);
        cursor = cursor->next; //mpve the cursor along the list
        count ++;
    } 
    
    return 0;
}

