#include <stdio.h>
#include <cs50.h>
int main(void)
{
    int values[] = {9,3,5,2,1,8,6,7,4};
    int n = 9;
     
  for (int i =0; i < n-1; i++)
    {
    for (int j = 0; j < n-1; j++)
        {
        if (values[j] > values[j+1])
           {
           int temp = values[j];
           values[j] = values [j+1];
           values[j+1] = temp;     
           }
        }
    }



    for (int v = 0; v < n; v++)
    {
        printf("%d", values[v]);
    
    }
    printf("\n");
}
