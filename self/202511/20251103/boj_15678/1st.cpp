#include <iostream>
#include <deque>
using namespace std;

int N, D;
long long ans = 0, cur, maxK = -1e9;
long long K[100'000];
deque<pair<long long, int>> q;

void solve() {
    cin >> N >> D;

    for (int idx = 0; idx < N; ++idx) cin >> K[idx];

    for (int idx = 0; idx < N; ++idx) {
        maxK = max(maxK, K[idx]);

        if (q.empty()) cur = K[idx];
        else cur = q[0].first + K[idx];

        if (cur < 0) cur = 0;

        ans = max(ans, cur);

        while (!q.empty() && idx - q[0].second >= D) q.pop_front();

        while (!q.empty() && q[q.size()-1].first <= cur) q.pop_back();

        q.emplace_back(cur, idx);
    }

    if (ans > 0) cout << ans << '\n';
    else cout << maxK << '\n';

    return;
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    solve();

    return 0;
}