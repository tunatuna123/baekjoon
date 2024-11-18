#include <bits/stdc++.h>
using namespace std;

int n, temp, m = 0, y = 0;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> temp;
        y += (temp/30 + 1) * 10;
        m += (temp/60 + 1) * 15;
    }
    if (m < y)
    {
        cout << "M " << m << endl;
    }
    else if (y < m)
    {
        cout << "Y " << y << endl;
    }
    else
    {
        cout << "Y M " << m << endl;
    }
    
    return 0;
}