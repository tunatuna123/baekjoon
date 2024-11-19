#include <bits/stdc++.h>
using namespace std;


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    int n;
    string a,b;
    cin >> n;
    while (n--)
    {
        int ans = 0;
        cin >> a;
        cin >> b;
        for (int i = 0; i < a.length(); i++)
        {
            if (a[i] != b[i])
            {
                ans++;
            }
        }
        cout << "Hamming distance is " << ans << ".\n";
    }
    return 0;
}