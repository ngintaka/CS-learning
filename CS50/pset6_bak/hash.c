#include <stdio.h>
#include <string.h>

int main(void)
{

    char* words[5] = {"absorbance", "absorbancy", "absorbant", "absorbed", "absorbefacient"};
    int char_sum = 0;
    int hash_value = 0;

    for (int i = 0; i < 5; i++)
    {
        char_sum = 0;
        for (int j = 0; j < strlen(words[i]); j++)
        {
            char_sum = char_sum + words[i][j];
        }
    hash_value = char_sum % 501;
    printf("Word: %s, char_sum: %d, hash_value: %d\n", words[i], char_sum, hash_value); 
         
    }


}
