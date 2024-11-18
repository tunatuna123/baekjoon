#include <stdio.h>

int main(){
    int n;
    int ans = 1;
    scanf("%d", &n);
    for (int i = 1; i <= n; i++)
    {
        ans *= i;
    }
    printf("%d", ans);
}