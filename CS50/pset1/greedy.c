#include <cs50.h>
#include <math.h>
#include <stdio.h>

int main(void)
{
    int quarters = 0, dimes = 0, nickels = 0, pennies = 0; //improves basic requirements by identifying quantity of each coin required
    int qval = 25, dval = 10, nval= 5, pval = 1;
    int total_coins = 0;
    float cents = 0;
    int change;

    do
    {
        printf("Oh hai! How much change is owed? ");
        cents = GetFloat() * 100;
    }
    while (cents <=0);
    
    change = (int)(round(cents));
    while (change > 0) {  //loop until all change accounted for
        while (change >= qval)
        {
            change = change - qval;
            quarters = quarters + 1;
        }
        while (change >= dval)
        {
            change = change - dval;
            dimes = dimes + 1;
        }
        while (change >= nval)
        {
            change = change - nval;
            nickels = nickels + 1;
        }
        while (change >= pval)
        {
            change = change - pval;
            pennies = pennies + 1;
        }
    }        
    
    total_coins = quarters + dimes + nickels + pennies; //sum individual coin totals
    
    /*printf("Total Coins: %d\n",total_coins);
    printf("Number of Quarters: %d\n",quarters);
    printf("Number of Dimes: %d\n",dimes);
    printf("Number of Nickels: %d\n",nickels);
    printf("Number of Pennies: %d\n",pennies);*/
    
    printf("%d\n",total_coins);
}

