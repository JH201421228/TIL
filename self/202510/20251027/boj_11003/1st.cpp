#include <iostream>
#include <deque>
using namespace std;


int N, L;
int arr[5'000'000];
int D[5'000'000];
deque<pair<int, int>> q;


void solve() {
    cin >> N >> L;

    for (int idx = 0; idx < N; ++idx) cin >> arr[idx];

    for (int idx = 0; idx < N; ++idx) {
        if (q.empty()) {
            q.emplace_back(arr[idx], idx);
        }
        else {
            if (idx - q.front().second >= L) {
                q.pop_front();
            }

            int cur = arr[idx];

            while (!q.empty() && q.back().first > cur) {
                q.pop_back();
            }

            q.emplace_back(cur, idx);
        }

        D[idx] = q.front().first;
    }

    for (int idx = 0; idx < N; ++idx) cout << D[idx] << ' ';

    return;
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    solve();

    return 0;
}