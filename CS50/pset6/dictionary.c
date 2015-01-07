/****************************************************************************
 * dictionary.c
 *
 * Computer Science 50
 * Problem Set 6
 *
 * Implements a dictionary's functionality.
 ***************************************************************************/
#include<string.h>
#include <stdbool.h>
#include "dictionary.h"

/**
 * Returns true if word is in dictionary else false.
 */

FILE* input;
int count = 0;
typedef struct node
{
    char word[LENGTH + 1];
    struct node* next;
}
node;  
node* dict[SIZE];

node* tmp;

bool check(const char* word)
{     
    char testword[strlen(word) + 1];
    for (int i = 0; i <= strlen(word); i++)
    {
        if (isalpha(word[i]) && isupper(word[i]))
        {
            testword[i] = tolower(word[i]);
        }
        else
        {
            testword[i] = word[i];
        }
    }

    long hashvalue = 0;
    for (int j = 0; j < strlen(testword); j++)
    {
         hashvalue = hashvalue + (501 * testword[j]); //sum ascii values of each character
    }            
    int idx = hashvalue % SIZE; //hash word to correct index for checking
    //printf("\nWord to find: %s; hash value: %d\n", word, idx);

    if (dict[idx] == 0) return false;
    
    else
        {
            //int ind = 0;
            node* cursor = dict[idx]; //add a node pointer that can traverse the linked list
            //int counter = 1;
            while (cursor != 0) //until we reach the tail
                {
                    //printf("\nWord being checked: %s\n", cursor->word);
                    if (strncmp(cursor->word, testword, SIZE) ==0) return true;
                        
                    else
                    {
                    cursor = cursor->next; //move the cursor along the list
                    //counter ++;
                    }
                    }
            }

    return false;
}

/**
 * Loads dictionary into memory.  Returns true if successful else false.
 */
bool load(const char* dictionary)
{
    int c = 0;
    input = fopen(dictionary, "r");
    if (input == NULL)
    {
        return -1;
    }
      
    char entry[LENGTH + 1];
    int z = 0;
    long hashvalue = 0;
    int index = 0;
for (int d = 0; d < SIZE; d++) dict[d] = 0; //initialize each dict pointer to NULL
   
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
            
            hashvalue = 0;
            for (int j = 0; j < strlen(entry); j++)
            {
                hashvalue = hashvalue + (501 * entry[j]); //sum ascii values of each character
            }
            
            index = hashvalue % SIZE; //hash to index

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
    return true;
}

/**
 * Returns number of words in dictionary if loaded else 0 if not yet loaded.
 */
unsigned int size(void)
{
    return count;
}

/**
 * Unloads dictionary from memory.  Returns true if successful else false.
 */
bool unload(void)
{
    for (int u = 0; u < SIZE; u++)
    {
        node* cursor = dict[u];
        if (cursor == 0) continue;
        
        else
        {
            while (cursor != 0)
            {
                node* temp = cursor;
                cursor = cursor->next;
                free(temp);
            }
        }
    }
    return true;
}
