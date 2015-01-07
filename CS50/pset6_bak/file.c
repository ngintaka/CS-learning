#include <stdio.h>

int main(void)
{
    FILE* input;
    FILE* output;
    int c;
    int count = 0;

    input = fopen("/home/cs50/pset6/dictionaries/large", "r");
    if (input == NULL)
    {
        return -1;
    }
    
    output = fopen("output.txt", "w");
    if (output == NULL)
    {
        return -2;
    }
    
    while(1)
    {
       c = fgetc(input); //returns character and progresses position pointer
       if (c == 10) count ++;
       if( feof(input) ) //if the end of the file is reached
       {
           break ;
       }
       fprintf(output, "%c", c);
       }
    fclose(input);
    fclose(output);
    printf("%d\n", count);
    return(0);
}

