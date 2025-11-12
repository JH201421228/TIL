#include <iostream>
#include <deque>
using namespace std;


int N, K;
int E[100'001];
long long dp[100'001], sums[100'001];
deque<int> q;


long long temp(int idx) {
    return dp[idx-1] - sums[idx];
}


void solve() {
    cin >> N >> K;

    for (int idx = 1; idx < N+1; ++idx) cin >> E[idx];

    for (int idx = 1; idx < N+1; ++idx) sums[idx] = sums[idx-1] + E[idx];

    for (int idx = 1; idx < N+1; ++idx) {
        while (!q.empty() && q.front() < idx-K) q.pop_front();

        while (!q.empty() && temp(q.back()) <= temp(idx)) q.pop_back();

        q.emplace_back(idx);

        dp[idx] = sums[idx] + temp(q.front());

        if (idx <= K) dp[idx] = max(dp[idx], sums[idx]);
    }

    cout << dp[N] << '\n';

    return;
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    solve();

    return 0;
}