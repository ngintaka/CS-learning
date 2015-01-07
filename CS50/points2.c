#include <stdio.h>
#include<string.h>

int main(int argc, char* argv[])
{
    printf("%s\n", argv[1]);
    printf("%p\n", &argv[1]);
       
    char* pscale = argv[1]; 
    printf("%c\n", *pscale);
    printf("%c\n", *(pscale + 2));
    printf("%p\n", pscale);
    printf("%s\n", pscale + 1);
    
    for (int i = 0; i < strlen(pscale); i++)
    printf("%c\n", *(pscale + i));
    
    char word[] = "robert";
    printf("word: %s\n", word);
    printf("word address: %p\n", &word);
    char *letter = &word[0];
    printf("letter: %p\n", letter);
    printf("last: %d\n", *(word+ 6));
    printf("%c\n", *word);
    
    
}
