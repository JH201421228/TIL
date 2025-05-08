#include <iostream>
#include <vector>
#include <queue>
using namespace std;


struct Edge {
    int x, c, d, inv;
    Edge() = default;
    Edge(int x, int c, int d, int inv) : x(x), c(c), d(d), inv(inv) {};
};

int N, src = 505, sink = 506, ans = 0, pre[507], dist[507], indx[507], checker[507], stories[3];
vector<Edge> G[507];

void set_edge(int u, int v, int c, int d) {
    G[u].emplace_back(v, c, -d, G[v].size());
    G[v].emplace_back(u, 0, d, G[u].size()-1);

    return;
}

int solve() {
    while (1) {
        fill(pre, pre+sink+1, -1); fill(indx, indx+sink+1, -1); fill(checker, checker+sink+1, 0); fill(dist, dist+sink+1, 1e9);
        queue<int> q; q.push(src); checker[src] = 1; dist[src] = 0;

        while (!q.empty()) {
            int n = q.front(); q.pop(); checker[n] = 0;

            for (int idx = 0; idx < G[n].size(); ++idx) {
                auto& edge = G[n][idx];

                if (edge.c and dist[edge.x] > dist[n] + edge.d) {
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

    return -ans - 3e6;
}

int main () {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> N;

    for (int i = 0; i < 3; ++i) cin >> stories[i];

    for (int v = 1; v < 4; ++v) {
        set_edge(src, v, 1, 1e6);
        set_edge(src, v, stories[v-1]-1, 0);
    }

    set_edge(src, 4, 1e9, 0);

    for (int u = 5; u < N+5; ++u) {
        int temp[3];
        for (int i = 0; i < 3; ++i) cin >> temp[i];

        set_edge(u, sink, 1, 0);

        for (int v = 1; v < 4; ++v) set_edge(v, u, 1, temp[v-1]);

        set_edge(4, u, 1, 0);
    }

    cout << solve() << '\n';

    return 0;
}