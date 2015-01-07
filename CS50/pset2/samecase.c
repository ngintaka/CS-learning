#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

string makesame(string s); //prototype

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
        if (!isalpha(k[c]))
        {
        printf("Usage: ./vigenere <keyword>\n");
        return 1;
        }
    }
    
    string key = makesame(k); //function call
    
    printf("%s\n", key);
    return 0;
    }
    
string makesame(string k)  //function definition
    {
    for (int c = 0; c <strlen(k); c++)
        {
        if (k[c] >= 'A' && k[c] <= 'Z')
            {
                k[c] = k[c] + ('a' -'A');
            }
        }    
    return k;
    }

    
    
    
  
