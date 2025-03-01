#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;


int N, M, C[203][203], F[203][203], D[203][203], maxv = 1<<30, pre[203], dist[203], checker[203], ans = 0;
vector<int> G[203];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> N >> M;

    for (int u = 101; u < 101+N; ++u) {
        cin >> C[u][202];
        G[u].emplace_back(202);
        G[202].emplace_back(u);
    }

    for (int u = 1; u < 1+M; ++u) {
        cin >> C[201][u];
        G[u].emplace_back(201);
        G[201].emplace_back(u);
    }

    for (int u = 1; u < 1+M; ++u) {
        for (int v = 101; v < 101+N; ++v) {
            cin >> D[u][v];
            D[v][u] = -D[u][v];

            G[u].emplace_back(v);
            G[v].emplace_back(u);

            C[u][v] = maxv;
        }
    }

    while (true) {
        fill(pre, pre+203, -1);
        fill(dist, dist+203, maxv);
        fill(checker, checker+203, 0);

        queue<int> q;
        q.push(201);
        dist[201] = 0;
        checker[201] = 1;

        while (!q.empty()) {
            int n = q.front();
            q.pop();
            checker[n] = 0;

            for (auto& x : G[n]) {
                if (C[n][x] - F[n][x] > 0 && dist[x] > dist[n] + D[n][x]) {
                    dist[x] = dist[n] + D[n][x];
                    pre[x] = n;

                    if (!checker[x]) {
                        q.push(x);
                        checker[x] = 1;
                    }
                }
            }
        }

        if (pre[202] == -1) break;
        
        int flow = maxv;

        for (int n = 202; n != 201; n = pre[n]) {
            flow = min(flow, C[pre[n]][n] - F[pre[n]][n]);
        }

        for (int n = 202; n != 201; n = pre[n]) {
            ans += (flow * D[pre[n]][n]);

            F[pre[n]][n] += flow;
            F[n][pre[n]] -= flow;
        }
    }

    cout << ans << '\n';

    return 0;
}