#include <bits/stdc++.h>
using namespace std;


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    int n;
    string s;
    map<string, string> m = {
        {"Algorithm", "204"},  
        {"DataAnalysis", "207"}, 
        {"ArtificialIntelligence", "302"}, 
        {"CyberSecurity", "B101"}, 
        {"Network", "303"}, 
        {"Startup", "501"}, 
        {"TestStrategy", "105"}
    };

    cin >> n;
    while (n--)
    {
        cin >> s;
        cout << m[s] << '\n';
    }
    
    return 0;
}