#include <iostream>
#include <unordered_set>
using namespace std;


int N;
int mask = 0;
int cand = 0;
int attemp = 0;
int nums[100'000];
unordered_set<int> S;


void solve() {
    cin >> N;

    for (int i = 0; i < N; ++i) cin >> nums[i];

    for (int i = 29; i >= 0; --i) {
        mask |= 1<<i;
        attemp = cand | (1<<i);

        S.clear();

        for (auto& n : nums) {
            int tmp = n & mask;
            if (S.find(tmp ^ attemp) != S.end()) {
                cand = attemp;
                break;
            }
            S.insert(tmp);
        }
    }

    cout << cand << '\n';

    return;
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    solve();

    return 0;
}