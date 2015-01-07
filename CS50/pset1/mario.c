#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int i, j;
    int height = 0;

    do
    {
        printf("Height: ");
        height = GetInt();
    }
    while (height > 23 || height < 1);

    
    int init_height = height + 2;
    while (height > 0)
    {
        for (i = 1; i < height; i++)
        {
            printf(" ");
        }
    
        for (j = (init_height - height); j > 0 ; j--)
        {
            printf("#");
        }    

    printf("\n");
    height--;
    }
    return 0;
}

