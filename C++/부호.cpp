#include <bits/stdc++.h>
using namespace std;

long long ans = 0, overflow = 0;
int n;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    for (int i = 0; i < 3; i++)
    {
        cin >> n;
        ans = 0;
        overflow = 0;
        
        for (int i = 0; i < n; i++)
        {
            long long tmp;
            cin >> tmp;
            if (ans > 0 and tmp > 0 and tmp > LLONG_MAX - ans)
            {
                overflow += 1;
            }
            if (ans < 0 and tmp < 0 and tmp < LLONG_MIN - ans)
            {
                overflow -= 1;
            }
            ans += tmp;
        }
        if (overflow < 0)
        {
            cout << '-' << endl;
        }
        else if (overflow > 0)
        {
            cout << '+' << endl;
        }
        else if (ans > 0)
        {
            cout << '+' << endl;
        }
        
        else if (ans < 0)
        {
            cout << '-' << endl;
        }
        else
        {
            cout << '0' << endl;
        }
        
    }
    
    return 0;
}