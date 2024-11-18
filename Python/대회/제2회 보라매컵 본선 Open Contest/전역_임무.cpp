#include <iostream>
#include <vector>
#include <algorithm>
#include <deque>
#include <cstdlib>

using namespace std;

int main() {
    int n, m, p;
    cin >> n >> m >> p;
    vector<vector<int>> stage;

    for (int i = 0; i < n; i++) {
        vector<int> row;
        for (int j = 0; j < m; j++) {
            int item;
            cin >> item;
            row.push_back(item);
        }
        stage.push_back(row);
    }

    for (auto i : stage) {
        if (find(i.begin(), i.end(), -1) != i.end()) {
            int items = count(i.begin(), i.end(), -1);
            deque<int> current_stage(i.begin(), i.end());
            sort(current_stage.begin() + items, current_stage.end());

            for (auto j : current_stage) {
                if (p >= j) {
                    p += j;
                } else if (p < j && p * 2 > j && items > 0) {
                    items--;
                    p *= 2;
                    p += j;
                } else {
                    cout << 0 << endl;
                    exit(0);
                }
            }
        } else {
            for (auto j : i) {
                if (p >= j) {
                    p += j;
                } else {
                    cout << 0 << endl;
                    exit(0);
                }
            }
        }
    }

    cout << 1 << endl;
    return 0;
}
