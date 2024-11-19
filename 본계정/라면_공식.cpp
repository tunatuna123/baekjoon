#include <bits/stdc++.h>
using namespace std;


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    int n,a,b,x;
    cin >> n;

    while (n--)
    {
        cin >> a >> b >> x;
        cout << a*(x-1) + b << '\n';
    }
    
    return 0;
}