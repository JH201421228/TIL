#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int N, src = 201, sink = 202, C[203][203], F[203][203], D[203][203], maxv = (1 << 31) - 1, ans = 0;
vector<int> G[203];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> N;

    for (int u = 1; u < N+1; ++u) {
        G[src].emplace_back(u);
        G[u].emplace_back(src);
        C[src][u] = 1;

        G[sink].emplace_back(u+100);
        G[u+100].emplace_back(sink);
        C[u+100][sink] = 1;
    }

    for (int u = 1; u < N+1; ++u) {
        for (int v = 101; v < N+101; ++v) {
            int d; cin >> d;
            
            G[u].emplace_back(v);
            G[v].emplace_back(u);
            C[u][v] = 1;
            D[u][v] = d; D[v][u] = -d;
        }
    }

    while (true) {
        int pre[203]; fill(pre, pre+203, -1);
        int dist[203]; fill(dist, dist+203, maxv);
        int checker[203]; fill(checker, checker+203, 0);
        
        queue<int> q; q.push(src); checker[src] = 1; dist[src] = 0;

        while (!q.empty()) {
            int n = q.front(); q.pop();
            checker[n] = 0;

            for (auto& x : G[n]) {
                if (C[n][x] > F[n][x] && dist[x] > dist[n] + D[n][x]) {
                    dist[x] = dist[n] + D[n][x];
                    pre[x] = n;

                    if (!checker[x]) {
                        checker[x] = 1;
                        q.push(x);
                    }
                }
            }
        }

        if (pre[sink] == -1) break;

        for (int n = sink; n != src; n = pre[n]) {
            F[pre[n]][n] += 1; F[n][pre[n]] -= 1;
            ans += D[pre[n]][n];
        }
    }

    cout << ans << '\n';

    return 0;
}