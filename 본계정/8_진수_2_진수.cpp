#include <bits/stdc++.h>
#define min(a, b)      (((a) < (b)) ? (a) : (b))
#define max(a, b)      (((a) > (b)) ? (a) : (b))
#define pi 3.14159265359
using namespace std;


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    string n;
    cin >> n;
    string ans = "";
    for (int i = 0; i < n.length(); i++)
    {
        if (n[i] == '0')
        {
            ans += "000";
        }
        else if (n[i] == '1')
        {
            ans += "001";
        }
        else if (n[i] == '2')
        {
            ans += "010";
        }
        else if (n[i] == '3')
        {
            ans += "011";
        }
        else if (n[i] == '4')
        {
            ans += "100";
        }
        else if (n[i] == '5')
        {
            ans += "101";
        }
        else if (n[i] == '6')
        {
            ans += "110";
        }
        else if (n[i] == '7')
        {
            ans += "111";
        }
    }
    cout << atoi(ans.c_str()) << '\n';
    return 0;
}