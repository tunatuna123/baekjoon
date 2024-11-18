#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    int n,i,ans; 
    string s;
    string v[7] = { "Never gonna give you up","Never gonna let you down","Never gonna run around and desert you","Never gonna make you cry","Never gonna say goodbye","Never gonna tell a lie and hurt you","Never gonna stop" };
    cin >> n; cin.ignore();
    
    while (n--)
    {
        cin >> s;
        for (i = 0; i < 7; i++)
            if (s == v[i])
                break;
        if (i == 7)
        {
            cout << "Yes";
            return 0;
        }
    }
    cout << "No";
}