/**
 * recover.c
 *
 * Computer Science 50
 * Problem Set 5
 *
 * Recovers JPEGs from a forensic image.
 */
#include <stdint.h> 
#include <stdio.h>
#include <stdlib.h>

int main(void)
{ 
    int n = 0;
    FILE* jpg = NULL;
    FILE* file = NULL;
    char name[8];
    
    typedef uint32_t HEAD;
    typedef uint32_t TAIL[15];
    
    typedef struct
    {
        HEAD head;
        TAIL tail;    
    }
    BLOCK;
    
    BLOCK block;
    
    file = fopen("card.raw", "r");
    if (file == NULL)
    {
        printf("Could not open card.raw.\n");
        return 2;
    }
             
    while (fread(&block, sizeof(block), 1, file) == 1)
    {       
        if (block.head == 0xe0ffd8ff || block.head == 0xe1ffd8ff)
        {
            if (jpg != NULL)
            {
                fclose(jpg);
            }
            sprintf(name, "%03d.jpg", n);
            jpg = fopen(name, "w");
            fwrite(&block, sizeof(block), 1, jpg);
            n++;
        }        
         
        else
        {
            if (jpg != NULL)
            {
                fwrite(&block, sizeof(block), 1, jpg);
            }            
        }
    
    }

    fclose(jpg);
    fclose(file);

    return 0;    
}

