#include <bits/stdc++.h>
using namespace std;

char num[5];
int ans;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    while (1)
    {
        ans = 0;
        cin >> num;
        if (num[0] == '0')
        {
            break;
        }
        for (int i = 0; i < strlen(num); i++)
        {
            if (num[i] == '1')
            {
                ans += 2;
            }
            else if (num[i] == '0')
            {
                ans += 4;
            }
            else
            {
                ans += 3;
            }
        }
        ans += strlen(num)+1;
        cout << ans << endl;
    }
    
    return 0;
}