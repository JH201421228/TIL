#include <iostream>
#include <vector>
#include <stack>
#include <queue>
using namespace std;

int N, K, O = 0, C = 0;
int V[1001], F[1001], U[1001], dp[1001], G[1001];
vector<int> cycle_parent[1001], cycle_child[1001];
stack<int> S;


int scc(int n) {
    int p = ++O;
    V[n] = O;
    S.push(n);

    int x = G[n];
    if (!V[x]) p = min(p, scc(x));
    else if (!F[x]) p = min(p, V[x]);

    if (p == V[n]) {
        ++C;

        while (!S.empty()) {
            int o = S.top(); S.pop();
            F[o] = C;
            U[C] += 1;

            if (o == n) break;
        }
    }

    return p;
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> N >> K;

    for (int idx = 1; idx < N+1; ++idx) cin >> G[idx];

    for (int n = 1; n < N+1; ++n) {
        if (!V[n]) scc(n);
    }

    for (int n = 1; n < N+1; ++n) {
        if (F[n] != F[G[n]]) {
            cycle_parent[F[G[n]]].emplace_back(F[n]);
            cycle_child[F[n]].emplace_back(F[G[n]]);
        }
    }

    dp[0] = 1;

    for (int x = 1; x < C+1; ++x) {
        if (cycle_child[x].empty()) {
            vector<int> temp;
            queue<int> q; q.push(x);

            while (!q.empty()) {
                int n = q.front(); q.pop();
                temp.emplace_back(n);

                for (int nxt : cycle_parent[n]) {
                    q.push(nxt);
                }
            }

            int dp_temp[1001];
            memcpy(dp_temp, dp, sizeof(dp));

            for (int n = U[temp[0]]; n < U[temp[0]] + temp.size(); ++n) {
                for (int idx = 0; idx < K; ++idx) {
                    if (dp[idx] && idx + n < K+1) dp_temp[idx + n] = 1;
                }
            }

            memcpy(dp, dp_temp, sizeof(dp));
        }
    }

    int ans = K;
    while (ans) {
        if (dp[ans]) break;

        ans -= 1;
    }

    cout << ans << '\n';

    return 0;
}