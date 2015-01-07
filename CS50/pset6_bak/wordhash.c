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
    for (int j = 0; j <= 25; j++) word[j] = 0;
    int z = 0;
    int char_sum = 0;
    int hash_value = 0;
    
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
            hash_value = char_sum % 501; // hash to index using large prime
            
            printf("Word: %s, char_sum: %d, hash_value: %d\n", word, char_sum, hash_value);                      
        }      
    }
 
    fclose(input);
    printf("\nWordcount: %d\n", count); //print final wordcount
    return(0);
}
