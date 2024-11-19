#include <bits/stdc++.h>
using namespace std;


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    int i,n,a,b,c;
    cin >> n;

    for (i = 0; i < n; i++)
    {
        cin >> a >> b >> c;
        cout << "Scenario #" << i+1 << ":\n";
        int m = max(a, max(b,c)), sum = 0;
        
        if (m == a)
        {
            sum = b*b + c*c;
        }
        else if (m == b)
        {
            sum = a*a + c*c;
        }
        else if (m == c)
        {
            sum = a*a + b*b;
        }

        if (m*m == sum)
        {
            cout << "yes\n\n";
        }
        else
        {
            cout << "no\n\n";
        }

    }
        if (i != n-1)
    {
        cout << '\n';
    }
}