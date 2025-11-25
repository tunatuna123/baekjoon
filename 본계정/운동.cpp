#include <bits/stdc++.h>
#define min(a, b)      (((a) < (b)) ? (a) : (b))
#define max(a, b)      (((a) > (b)) ? (a) : (b))
#define pi 3.14159265359
using namespace std;


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    int N,m,M,T,R;
    cin >> N >> m >> M >> T >> R;
    if (m + T > M)
    {
        cout << -1 << '\n';
        return 0;
    }   

    int ans = 0;
    int cur = m;
    while (N)
    {
        if (cur + T <= M)
        {
            cur += T;
            N--;
        }
        else
        {
            cur = max(m, cur - R);
        }
        ans++;
    }
    cout << ans << '\n';

    return 0;
}