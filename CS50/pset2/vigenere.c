#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, string argv[])
{
    if (argc != 2)  //check for correct # of args
    {
        printf("Usage: ./vigenere <keyword>\n");
        return 1;
    }
    string k = argv[1];
    
    for (int c = 0; c < strlen(k); c++)
    {
        if (!isalpha(k[c]))  //check that key input is alpha
        {
        printf("Usage: ./vigenere <keyword>\n");
        return 1;
        }
    }
    //printf("input plaintext: "); //get user input
    string p = GetString();

    for (int n = 0; n <strlen(k); n++) //loop to convert uppercase key chars to lower
        {
        if (k[n] >= 'A' && k[n] <= 'Z')
            {
                k[n] = k[n] + ('a' -'A'); 
            }
        }

    int l = strlen(k); //use modulo of key length to recycle key characters

    
    for (int i = 0, j = 0; i < strlen(p); i++)
    {
        if (p[i] >= 'a' && p[i] <= 'z') //if plaintext is lower
        {
                printf("%c", ('a' + (p[i]- 'a' + (k[j%l])- 'a')%26));
                j++;
        }
        
        else if (p[i] >= 'A' && p[i] <= 'Z')   //if plaintext is upper
        {
                printf("%c", ('A' + (p[i] - 'A' + k[j%l]- 'a')%26));
                j++;        
        }
        
        else //if plaintext is not alpha   
        {
           printf("%c", p[i]); 
        }    
    }
    printf("\n");
    return 0;
}
  
