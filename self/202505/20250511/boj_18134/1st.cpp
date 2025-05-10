#include <iostream>
#include <vector>
#include <queue>
using namespace std;


struct Edge {
    int x, c, d, inv;
    Edge() = default;
    Edge(int x, int c, int d, int inv) : x(x), c(c), d(d), inv(inv) {};
};

int N, M, src, sink, ans = 0, pre[2002], dist[2002], indx[2002], checker[2002];
vector<Edge> G[2002];

void set_edge(int u, int v, int c, int d) {
    G[u].emplace_back(v, c, d, G[v].size());
    G[v].emplace_back(u, 0, -d, G[u].size()-1);

    return;
}

int solve() {
    fill(pre, pre+2002, -1); fill(checker, checker+2002, 0); fill(indx, indx+2002, -1); fill(dist, dist+2002, 1e9);
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

    if (pre[sink] == -1) return dist[sink];

    for (int n = sink; n != src; n = pre[n]) {
        auto& edge = G[pre[n]][indx[n]];
        --edge.c;
        ++G[n][edge.inv].c;
    }

    return dist[sink];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> N >> M;

    for (int u = 1; u < N+1; ++u) set_edge(u<<1, u<<1|1, 1, 0);

    for (int i = 0; i < M; ++i) {
        int a, b, c; cin >> a >> b >> c;
        set_edge(b<<1|1, c<<1, 1, a);
        set_edge(c<<1|1, b<<1, 1, a);
    }

    int a, b; cin >> a >> b;
    src = a<<1; sink = b<<1|1;
    set_edge(a<<1, a<<1|1, 1, 0);
    set_edge(b<<1, b<<1|1, 1, 0);

    for (int i = 0; i < 2; ++i) ans += solve();

    if (ans >= 1e9) cout << -1 << '\n';
    else cout << ans << '\n';

    return 0;
}