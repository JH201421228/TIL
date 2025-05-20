#include <iostream>
#include <vector>
#include <queue>
using namespace std;


struct Edge {
    int x, c, d, inv;
    Edge() = default;
    Edge(int x, int c, int d, int inv) : x(x), c(c), d(d), inv(inv) {};
};


int T, src = 1002, sink = 1003, ans, N, M, pre[1004], dist[1004], checker[1004], indx[1004], coins[500], nodes[500]; 
vector<Edge> G[1004];


void set_edge(int u, int v, int c, int d) {
    G[u].emplace_back(v, c, d, G[v].size());
    G[v].emplace_back(u, 0, -d, G[u].size()-1);

    return;
}


int solve() {
    ans = 0;

    while (1) {
        fill(pre, pre+1004, -1); fill(indx, indx+1004, -1); fill(dist, dist+1004, 1e9); fill(checker, checker+1004, 0);
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

        for (int n = sink; n != src; n = pre[n]) {
            auto& edge = G[pre[n]][indx[n]];
            --edge.c;
            ++G[n][edge.inv].c;
        }

        ans += dist[sink];
    }

    return ans;
}


int main () {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> T;

    while (T--) {
        cin >> N >> M;

        for (int idx = 0; idx < sink+1; ++idx) G[idx].clear();

        for (int u = 1; u < N+1; ++u) set_edge(u<<1, u<<1|1, 1e9, 0);

        for (int i = 0; i < M; ++i) {
            int x, y; cin >> x >> y;
            set_edge(x<<1|1, y<<1, 1e9, 1); set_edge(y<<1|1, x<<1, 1e9, 1);
        }

        for (int idx = 0; idx < N; ++idx) cin >> nodes[idx];
        for (int idx = 0; idx < N; ++idx) cin >> coins[idx];

        for (int u = 1; u < N+1; ++u) {
            if (!nodes[u-1]) set_edge(u<<1|1, sink, 1, 0);
        }

        for (int v = 1; v < N+1; ++v) {
            if (!coins[v-1]) set_edge(src, v<<1, 1, 0);
        }

        cout << solve() << '\n';
    }

    return 0;
}