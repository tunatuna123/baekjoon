#include <stdio.h>

int main(){
    int n,a;
    int ans = 0;
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &a);
        ans += a;
    }
    printf("%d", ans-(n-1));
}