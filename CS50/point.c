#include <stdio.h>

int main(void)
{
    int* px;
    int* py;
    int** ppx;
    int** ppy;
    int x = 3;
    int y = 4;
    px = &x;
    py = &y;
    ppx = &px;
    ppy = &py;
    
    printf("\nx: %p\ny: %p\n", &x, &y);
    printf("Size of x: %d\n", sizeof(x));
    printf("\npx: %p\npy: %p\n add_px: %p", px, py, &px);
    printf("\nx: %x\ny: %x\n\n", *px, *py);
    printf("\nppx: %p\nppy: %p\n\n", ppx, ppy);
    
    printf("Plus 1: %p\n\n", ppx +1);
    printf("Size of ppx: %d\n\n", sizeof(ppx));
    
    printf("Char: %d\nInt: %d\nLong: %d\nFloat: %d\nDouble:  %d\n", sizeof(char), sizeof(int), sizeof(long), sizeof(float), sizeof(double));
    

return 0; 
}

