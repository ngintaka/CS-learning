#include <stdio.h>
#include <cs50.h>
int main(void)
{
    int values[] = {1542, 7722, 11995, 12633, 24446, 29533, 35698, 37119, 46509, 48311};
    int n = 10;
    int value = 7722;
    int min = 0;
    int max = n;
    int v = (max+min)/2;
  
    while (max - min > 1)
    {
        
    if (values[v] == value)
        {
        printf("Yup, found %d\n", value);
        return 0;
        }
    else if (values[v] > value)
        {
        max = v;
        v = (max+min)/2;
        }       
    else
        {
        min = v;
        v = (max+min)/2;
        }
    }
        
   printf("Nope, not here\n");                     
}
