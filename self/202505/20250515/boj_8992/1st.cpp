#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;


struct Edge {
    int x, c, d, inv;
    Edge() = default;
    Edge(int x, int c, int d, int inv) : x(x), c(c), d(d), inv(inv) {};
};

int T, N, M, src = 401, sink = 402, ans, cnt;
int pre[403], dist[403], indx[403], checker[403];
vector<Edge> G[403];
int vertical[401][5], horizontal[401][5];

void set_edge(int u, int v, int c, int d) {
    G[u].emplace_back(v, c, -d, G[v].size());
    G[v].emplace_back(u, 0, d, G[u].size()-1);

    return;
}

void solve() {
    ans = 0; cnt = 0;

    while (1) {
        fill(pre, pre+403, -1); fill(indx, indx+403, -1); fill(checker, checker+403, 0); fill(dist, dist+403, 1e9);
        queue<int> q; q.push(src); checker[src] = 1; dist[src] = 0;

        while (!q.empty()) {
            int n = q.front(); q.pop(); checker[n] = 0;

            for (int idx = 0; idx < G[n].size(); ++idx) {
                auto& edge = G[n][idx];

                if (edge.c && dist[edge.x] > dist[n] + edge.d) {
                    dist[edge.x] = dist[n] + edge.d; pre[edge.x] = n; indx[edge.x] = idx;

                    if (!checker[edge.x]) {
                        checker[edge.x] = 1; q.push(edge.x);
                    }
                }
            }
        }

        if (pre[sink] == -1) break;

        ++cnt;

        for (int n = sink; n != src; n = pre[n]) {
            auto& edge = G[pre[n]][indx[n]];
            --edge.c;
            ++G[n][edge.inv].c;
        }

        ans += dist[sink];
    }

    return;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> T;

    while (T--) {
        cin >> N >> M;
        
        for (int i = 1; i < N+1; ++i) {
            for (int j = 0; j < 5; ++j) {
                cin >> horizontal[i][j];
            }
        }

        for (int i = 201; i < M+201; ++i) {
            for (int j = 0; j < 5; ++j) {
                cin >> vertical[i][j];
            }
        }

        for (int idx = 0; idx < 403; ++idx) G[idx].clear();

        for (int u = 1; u < N+1; ++u) {
            int u_x1 = horizontal[u][0], u_y1 = horizontal[u][1], u_x2 = horizontal[u][2], u_y2 = horizontal[u][3], u_w = horizontal[u][4];
            set_edge(src, u, 1, 0);

            for (int v = 201; v < M+201; ++v) {
                int v_x1 = vertical[v][0], v_y1 = vertical[v][1], v_x2 = vertical[v][2], v_y2 = vertical[v][3], v_w = vertical[v][4];

                if (v_x1 > min(u_x1, u_x2) && v_x1 < max(u_x1, u_x2) && u_y1 > min(v_y1, v_y2) && u_y1 < max(v_y1, v_y2)) {
                    set_edge(u, v, 1, u_w*v_w);
                }
            }
        }

        for (int v = 201; v < M+201; ++v) set_edge(v, sink, 1, 0);

        solve();

        cout << cnt << ' ' << -ans << '\n';
    }

    return 0;
}