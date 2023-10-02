#include <bits/stdc++.h>
using namespace std;

int n;
int arr[3] = {1,2,3};
int p,q;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> p >> q;
        swap(arr[p-1], arr[q-1]);
    }
    for (int i = 0; i < 3; i++)
    {
        if(arr[i] == 1){
            cout << i+1 << endl;
        }
    }
    
    return 0;
}