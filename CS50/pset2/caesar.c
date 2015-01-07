#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, string argv[])
{
    if (argc != 2)  //check for correct # of args
    {
        printf("Caesar takes a single non-negative integer as an argument\n");
        return 1;
    }
      
    int k = atoi(argv[1]);

    if (k < 0)  //check for non-negative integer
    {
        printf("Caesar takes a single non-negative integer as an argument\n");
        return 1;
    }

//    printf("What is the string to encode?\n");
    string plaintext = GetString();

//encode both upper & lower case letters but not punctuation

    for (int i = 0; i < strlen(plaintext); i++)
    {
        if (plaintext[i] >= 'a' && plaintext[i] <= 'z')
        {
            printf("%c",(97 + (plaintext[i]-97 + k)%26));
        }
    
        else if (plaintext[i] >= 'A' && plaintext[i] <= 'Z')
        {
            printf("%c",(65 + (plaintext[i]-65 + k)%26));       
        }
        else
        {
            printf("%c", plaintext[i]);
        
        }

    }

    printf("\n");
   
    return 0;
}

