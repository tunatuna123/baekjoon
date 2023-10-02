#include <bits/stdc++.h>
using namespace std;

int a,b;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    
    cin >> a >> b;
    if (a > b)
    {
        swap(a,b);
    }
    cout << ((b-1)/4-(a-1)/4) + (max((a-1)%4,(b-1)%4) - min((a-1)%4,(b-1)%4)) << endl;
    return 0;
}