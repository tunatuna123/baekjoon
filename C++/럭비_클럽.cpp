#include <bits/stdc++.h>
using namespace std;

char name[11];
int age, weight;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    
    while (1)
    {
        cin >> name >> age >> weight;
        if (name[0] == '#' and age == 0 and weight == 0)
        {
            break;
        }
        
        if (age > 17 or weight >= 80)
        {
            cout << name << " Senior" << endl;
        }
        else
        {
            cout << name << " Junior" << endl;
        }
    }
    
}