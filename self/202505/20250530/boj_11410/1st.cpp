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

int N, P, src = 51, sink = 52, ans, pre[53], dist[53], checker[53], indx[53], clients[49][49], fees[49][49];
vector<Edge> G[53];

void set_edge(int u, int v, int c, int d) {
    G[u].emplace_back(v, c, -d, G[v].size());
    G[v].emplace_back(u, 0, d, G[u].size()-1);

    return;
}

void solve() {
    ans = 0;

    while (1) {
        fill(pre, pre+53, -1); fill(indx, indx+53, -1); fill(checker, checker+53, 0); fill(dist, dist+53, 1e9);
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

        int flow = 1e9;
        for (int n = sink; n != src; n = pre[n]) {
            auto& edge = G[pre[n]][indx[n]];
            flow = min(flow, edge.c);
        }

        for (int n = sink; n != src; n = pre[n]) {
            auto& edge = G[pre[n]][indx[n]];
            edge.c -= flow;
            G[n][edge.inv].c += flow;
        }

        ans += dist[sink]*flow;
    }

    return;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> N >> P;
    
    set_edge(src, 1, P, 0); set_edge(N, sink, P, 0);
    for (int u = 1; u < N; ++u) set_edge(u, u+1, 1e9, 0);

    for (int i = 0; i < N-1; ++i) {
        for (int j = 0; j < N-1-i; ++j) cin >> clients[i][j];
    }

    for (int i = 0; i < N-1; ++i) {
        for (int j = 0; j < N-1-i; ++j) cin >> fees[i][j];
    }

    for (int u = 1; u < N; ++u) {
        for (int v = u+1; v < N+1; ++v) set_edge(u, v, clients[u-1][v-u-1], fees[u-1][v-u-1]);
    }

    solve();

    cout << -ans << '\n';

    return 0;
}