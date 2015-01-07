#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#define LENGTH 45

int main(void)
{
    FILE* input;
    int c = 0;
    int count = 0;

    input = fopen("large", "r");
    if (input == NULL)
    {
        return -1;
    }
      
    char word[LENGTH + 1];
    for (int j = 0; j <= LENGTH; j++) word[j] = 0;
    int z = 0;
    int char_sum = 0;
    int index = 0;

    typedef struct node
    {
        char word[LENGTH + 1];
        struct node* next;
    }
    node;  
    node* head = NULL;
    

    while (1)
    {
       c = fgetc(input); //returns character and progresses position pointer
       if (c == EOF) break; // end if reach end of file
       if (isalpha(c) || (c == '\'' && z > 0))
       {
        word[z] = c; //add characters to word one by one
        z++;       
       }
       if (c == 10) // if hit a line break (ie end of word)
       {
            word[z] = '\0';
            count ++; // increment wordcount
            z = 0; //reset character index for next word
            //printf("%s\n", word); //check we've found a word
            
            char_sum = 0;
            for (int j = 0; j < strlen(word); j++)
            {
                char_sum = char_sum + word[j]; //sum ascii values of each character
            }
            index = char_sum % 501; // hash to index using large prime

            node* index = malloc(sizeof(node));
            strcpy(index->word, word); // need to use strcpy to fill node with text
        
            if (head == NULL)
            {
                head = index; //set pointer to first node
                index->next = NULL; //first node is end of list
            }
        
            else
            {
                index->next = head; // push new pointers to head of linked list
                head = index;
            }
        }      
    }
 
    fclose(input);
    printf("\nTraversing the linked list node by node...\n");
    
    node* cursor = head; //add a node pointer that can traverse the linked list
    int counter = 1;
    while (cursor != 0) //until we reach the tail
    {
        printf("Word #%d is: %s\n", counter, cursor->word);
        cursor = cursor->next; //move the cursor along the list
        counter ++;
    } 

    printf("\nFinal Wordcount: %d\n", count); //print final wordcount
    return(0);
}
