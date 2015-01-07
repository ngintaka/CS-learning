#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define LENGTH 45
#define SIZE 100

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
      
    char entry[LENGTH + 1];
    int z = 0;
    int char_sum = 0;
    int index = 0;

    typedef struct node
    {
        char word[LENGTH + 1];
        struct node* next;
    }
    node;  

    node* dict[SIZE];
    for (int d = 0; d < SIZE; d++) dict[d] = 0; //initialize each dict pointer to NULL
    
    node* tmp;
    
    while (1)
    {
       c = fgetc(input); //returns character and progresses position pointer
       if (c == EOF) break; //end if reach end of file
       
       if (isalpha(c) || (c == '\'' && z > 0))
       {
        entry[z] = c; //add characters to entry one by one
        z++;       
       }
       
       else if (c == 10) //if hit a line break (ie end of entry)
       {
            entry[z] = '\0';
            count ++; //increment wordcount
            z = 0; //reset character index for next entry
            //printf("\nFound an entry: %s\n", entry); //check we've found a word
            
            char_sum = 0;
            for (int j = 0; j < strlen(entry); j++)
            {
                char_sum = char_sum + entry[j]; //sum ascii values of each character
            }
            
            index = char_sum % SIZE; //hash to index

            if (dict[index] == 0)
            {
                dict[index]= malloc(sizeof(node));
                strcpy(dict[index]->word, entry);
                //printf("Node: %d, First word: %s\n", index, dict[index]->word);
                dict[index]->next = 0;                
            }
        
            else
            {
                tmp = dict[index];
                dict[index]= malloc(sizeof(node));
                strcpy(dict[index]->word, entry);
                //printf("Node: %d, Next word: %s\n", index, dict[index]->word);
                dict[index]->next = tmp;
           }
        }      
    }
 
    fclose(input);
    //printf("\nTraversing the linked list node by node...\n");
    
    for (int ind = 0; ind < SIZE; ind++)
    {
        if (dict[ind]->word)
            {
                node* cursor = dict[ind]; //add a node pointer that can traverse the linked list
                int counter = 1;
                while (cursor != 0) //until we reach the tail
                    {
                        //printf("Node is:%d; Word #%d is: %s\n", ind, counter, cursor->word);
                        cursor = cursor->next; //move the cursor along the list
                        counter ++;
                    }
            }
    }
    printf("\nFinal Wordcount: %d\n", count); //print final wordcount
    return(0);
}

