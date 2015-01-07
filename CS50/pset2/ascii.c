#include <stdio.h>

int main()
{
    int i;
    int *p;   /* a pointer to an integer */
    printf("%d %d\n", p, &i);
    p = &i;
    printf("%d %d\n", p, &i);
    return 0;
}
