#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> tower(n);
    for (int i = 0; i < n; i++) {
        cin >> tower[i];
    }
    
    while (true) {
        bool flag = false;
        for (int i = 1; i < tower.size(); i++) {
            if (tower[i] < tower[i-1]) {
                tower[i] = -1;
                flag = true;
            }
        }
        if (!flag) {
            break;
        }
        vector<int> new_tower;
        for (int i = 0; i < tower.size(); i++) {
            if (tower[i] != -1) {
                new_tower.push_back(tower[i]);
            }
        }
        tower = new_tower;
    }
    
    cout << tower.size() << endl;
    return 0;
}