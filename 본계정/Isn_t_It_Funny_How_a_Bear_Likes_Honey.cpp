#include <bits/stdc++.h>
#define min(a, b)      (((a) < (b)) ? (a) : (b))
#define max(a, b)      (((a) > (b)) ? (a) : (b))
#define pi 3.14159265359
using namespace std;


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    int n, b;
    double w, r;
    cin >> n;

    for(int i = 0; i < n; i++)
    {
        cin >> b >> w;
        double ans = 0;
        while (b--)
        {
            cin >> r;
            ans += 4.0/3.0*pow(r,3)*pi/1000;
        }

        cout << "Data Set " << i+1 << ":" << endl;
        if (w <= ans)
        {
            cout << "Yes\n" << endl;
        }
        else
        {
            cout << "No\n" << endl;
        }
    }
    return 0;
}