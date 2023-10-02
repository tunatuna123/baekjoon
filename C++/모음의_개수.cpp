#include <bits/stdc++.h>
using namespace std;

int ans;
char s[256];

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    while (1)
    {
        ans = 0;
        cin.getline(s,256);

        if (s[0] == '#')
        {
            break;
        }
        for (int i = 0; i < strlen(s)-1; i++)
        {
            if ((char) tolower(s[i]) == 'a' or (char) tolower(s[i]) == 'e' or (char) tolower(s[i]) == 'i' or (char) tolower(s[i]) == 'o' or (char) tolower(s[i]) == 'u')
            {
                ans ++;
            }
            
        }
        cout << ans << endl;
    }
    
}