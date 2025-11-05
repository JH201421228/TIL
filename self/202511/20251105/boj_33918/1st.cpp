#include <iostream>
#include <queue>
using namespace std;


int N, M, C, D, ans = 1e-9;
int B[200];
int dp[200][25'001];
priority_queue<pair<int, int>> pq;


void solve() {
    for (int time = 0; time < N; ++time) {
        for (int temp = 1; temp < M+1; ++temp) {
            dp[time][temp] = M - abs(temp - B[time]);
        }
    }

    for (int time = 0; time < N-1; ++time) {
        for (int offset = 1; offset < C+1; ++offset) {
            while (!pq.empty()) pq.pop();

            for (int temp = offset; temp < min(offset + D, M) + 1; temp += C) {
                pq.emplace(dp[time][temp], temp);
            }

            for (int temp = offset; temp < M+1; temp += C) {
                if (temp != offset && temp+D < M+1) pq.emplace(dp[temp][temp+D], temp+D);

                while (!pq.empty() && pq.top().second + D < temp) pq.pop();

                dp[time+1][temp] += pq.top().first;
            }
        }
    }

    for (int idx = 0; idx < M+1; ++idx) ans = max(ans, dp[N-1][idx]);

    cout << ans << '\n';

    return;
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> N >> M >> C >> D;
    for (int idx = 0; idx < N; ++idx) cin >> B[idx];

    solve();

    return 0;
}