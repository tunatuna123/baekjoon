#include <stdio.h>
int main(void)
{
    int a, array[751][751] = {}, i = 0, j = 0, flag = 1;

    scanf("%d", &a);

    for (int k = 1; k <= a*a; k++)
    {
        array[i][j] = k;

        if (flag == 1)
        {
            j++;
            if (j == a || array[i][j]!=0)
            {
                flag = 2;
                j--;
                i++;    
                continue;
            }
        }

        else if (flag == 2)
        {
            i++;
            if (i == a || array[i][j] != 0)
            {
                flag = 3;
                i--;
                j--;
                continue;
            }
        }
 
        else if (flag == 3)
        {
            j--;
            if (j < 0 || array[i][j] != 0)
            {
                flag = 4;
                j++;
                i--;
                continue;
            }
        }
 
        else if (flag == 4)
        {
            i--;
            if (i < 0 || array[i][j] != 0)
            {
                flag = 1;
                j++;
                i++;
                continue;
            }
        }
    }

    for (int i = 0; i < a; i++)
    {
        for (int j = 0; j < a; j++)
        {
            printf("%d ", array[i][j]);
        }
        printf("\n");
    }
    return 0;
}
