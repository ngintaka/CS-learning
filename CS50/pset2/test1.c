#include <stdio.h>
#include <cs50.h>
#include <string.h>

int main(void)
{
    string k = "bacon";
    int l = strlen(k);
    for (int i = 0; i < 10; i++)
    {
        printf("%c\n", k[i%l]);
    }
}    
