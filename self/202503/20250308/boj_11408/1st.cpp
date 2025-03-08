#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int N, M, maxv = 1<<31-1, F[803][803], C[803][803], D[803][803], src = 801, sink = 802, pre[803], dist[803], checker[803], ans = 0, cnt = 0;
vector<int> G[803];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> N >> M;

    for (int u = 1; u < N+1; ++u) {
        G[src].emplace_back(u);
        G[u].emplace_back(src);
        C[src][u] = 1;
    }

    for (int u = 401; u < M+401; ++u) {
        G[sink].emplace_back(u);
        G[u].emplace_back(sink);
        C[u][sink] = 1;
    }

    for (int u = 1; u < N+1; ++u) {
        int t; cin >> t;
        for (int j = 0; j < t; ++j) {
            int v, c; cin >> v >> c;
            G[v+400].emplace_back(u);
            G[u].emplace_back(v+400);
            C[u][v+400] = 1;
            D[u][v+400] = c; D[v+400][u] = -c;
        }
    }

    while (true) {
        fill(pre, pre+803, -1);
        fill(dist, dist+803, maxv);
        fill(checker, checker+803, 0);
        queue<int> q; q.push(src);
        
        checker[src] = 1; dist[src] = 0;

        while (!q.empty()) {
            int n = q.front(); q.pop();
            checker[n] = 0;

            for (auto& x : G[n]) {
                if (C[n][x] - F[n][x] > 0 && dist[x] > dist[n] + D[n][x]) {
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
            F[pre[n]][n] += 1;
            F[n][pre[n]] -= 1;
            ans += D[pre[n]][n];
        }
    }

    for (int i = 0; i < 803; ++i) {
        if (F[i][sink] == 1) {
            cnt += 1;
        }
    }

    cout << cnt << '\n' << ans << '\n';

    return 0;
}