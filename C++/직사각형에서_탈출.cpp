#include <bits/stdc++.h>
using namespace std;

int x,y,h,w;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> x >> y >> w >> h;
    cout << min(min(w-x, h-y), min(x,y)) << endl;
    return 0;
}