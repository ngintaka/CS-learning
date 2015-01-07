#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
    char* strings[] = {"dog", "cat", "pig", "cow", "bat"};
    int length = sizeof(strings)/sizeof(strings[0]);
    
    typedef struct node
    {
        char word[10];
        struct node* next;
    }
    node;  
    node* head = NULL;
    
    for (int i = 0; i < length; i++)
    {
        node* n = malloc(sizeof(node));
        strcpy(n->word, strings[i]); // need to use strcpy to fill node with text
        
        if (head == NULL)
        {
            head = n; //set pointer to first node
            head->next = NULL; //first node is end of list
        }
        
        else
        {
            n->next = head; // push new pointers to head of linked list
            head = n;
        }
        
        //printf("Node word: %s\n", n->word);
        //printf("Next node: %p\n", n->next);
        //printf("Head: %p\n", head);
        //printf("Head node word: %s\n", head->word);
    }
        
    printf("\nTraversing the linked list node by node...\n");
    
    node* cursor = head; //add a node pointer that can traverse the linked list
    int count = 1;
    while (cursor != 0)
    {
        printf("Word #%d is: %s\n", count, cursor->word);
        cursor = cursor->next; //mpve the cursor along the list
        count ++;
    }   
}
