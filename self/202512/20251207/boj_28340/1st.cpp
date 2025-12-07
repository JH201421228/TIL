#include <iostream>
#include <queue>
using namespace std;


int T, N, K;
priority_queue<long long> pq;


void solve() {
    cin >> N >> K;
    while (pq.size() > 0) pq.pop();

    for (int i = 0; i < N; ++i) {
        int tmp; cin >> tmp; pq.push(-tmp);
    }

    while ((N-1) % (K-1)) {
        pq.push(0);
        ++N;
    }

    long long ans = 0;
    while (pq.size() > 1) {
        long long cur = 0;

        for (int i = 0; i < K; ++i) {
            cur -= pq.top();
            pq.pop();
        }

        ans += cur;
        pq.push(-cur);
    }

    cout << ans << '\n';

    return;
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> T;

    while (T--) solve();

    return 0;
}