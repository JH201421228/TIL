#include <iostream>
#include <vector>
#include <queue>
#include <cmath>
#include <cstring>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    while (true) {
        int N, M;
        cin >> N >> M;
        if (N == 0 && M == 0) break;

        vector<string> maps(N);
        for (int i = 0; i < N; ++i) {
            cin >> maps[i];
        }

        vector<pair<int, int>> homes, children;
        for (int i = 0; i < N * M; ++i) {
            int r = i / M;
            int c = i % M;
            if (maps[r][c] == 'H') {
                homes.emplace_back(r, c);
            } else if (maps[r][c] == 'm') {
                children.emplace_back(r, c);
            }
        }

        int n = homes.size();
        int m = children.size();
        int src = n + m + 1;
        int sink = n + m + 2;
        int node_count = sink + 1;

        vector<vector<int>> G(node_count);
        vector<vector<int>> F(node_count, vector<int>(node_count, 0));
        vector<vector<int>> C(node_count, vector<int>(node_count, 0));
        vector<vector<int>> D(node_count, vector<int>(node_count, 0));

        for (int i = 0; i < n; ++i) {
            int u = i + 1;
            G[src].push_back(u);
            G[u].push_back(src);
            C[src][u] = 1;
        }

        for (int i = 0; i < m; ++i) {
            int u = i + 1 + n;
            G[u].push_back(sink);
            G[sink].push_back(u);
            C[u][sink] = 1;
        }

        for (int i = 0; i < n; ++i) {
            int u = i + 1;
            auto [hr, hc] = homes[i];
            for (int j = 0; j < m; ++j) {
                int v = j + 1 + n;
                auto [cr, cc] = children[j];
                int cost = abs(hr - cr) + abs(hc - cc);
                G[u].push_back(v);
                G[v].push_back(u);
                C[u][v] = 1;
                D[u][v] = cost;
                D[v][u] = -cost;
            }
        }

        int ans = 0;

        while (true) {
            vector<int> pre(node_count, -1);
            vector<int> dist(node_count, 1e9);
            vector<int> in_queue(node_count, 0);
            queue<int> q;
            q.push(src);
            dist[src] = 0;
            in_queue[src] = 1;

            while (!q.empty()) {
                int u = q.front(); q.pop();
                in_queue[u] = 0;
                for (int v : G[u]) {
                    if (C[u][v] > F[u][v] && dist[v] > dist[u] + D[u][v]) {
                        dist[v] = dist[u] + D[u][v];
                        pre[v] = u;
                        if (!in_queue[v]) {
                            in_queue[v] = 1;
                            q.push(v);
                        }
                    }
                }
            }

            if (pre[sink] == -1) break;

            for (int v = sink; v != src; v = pre[v]) {
                F[pre[v]][v]++;
                F[v][pre[v]]--;
                ans += D[pre[v]][v];
            }
        }

        cout << ans << '\n';
    }

    return 0;
}
