#include <bits/stdc++.h>
#define min(a, b)      (((a) < (b)) ? (a) : (b))
#define max(a, b)      (((a) > (b)) ? (a) : (b))
#define pi 3.14159265359
using namespace std;


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    int n, l = 1;
    string s, t;
    cin >> n;

    while (n--)
    {
        cin >> s;
        if (s.size() >= l)
        {
            cout << s[l-1];
        }
        else
        {
            cout << " ";
        }
        l = s.size();
    }
    cout << '\n';
    return 0;
}