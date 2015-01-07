/**
 * helpers.c
 *
 * Computer Science 50
 * Problem Set 3
 *
 * Helper functions for Problem Set 3.
 */
       
#include <cs50.h>
#include "helpers.h"
#include <stdio.h>

/**
 * Returns true if value is in array of n values, else false.
 */

/** Linear search for unsorted array.

bool search(int value, int values[], int n)
{     
    if (n <= 0)
        return false;
      
    for (int i = 0; i <= n;)
        {
        if (values[i] == value)
            return true;
        else 
           i++;
        }
    return false;
}   
*/

/** Binary search for sorted array.*/

bool search(int value, int values[], int n)
{
    int min = 0;
    int max = n;
    int v = (max+min)/2;
  
    while (max - min > 1)
    {
        
    if (values[v] == value)
        return true;
        
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
 return false;     
}

/**
 * Uses Bubble Sort to sort array of n values.
 */
void sort(int values[], int n)
{
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
}

