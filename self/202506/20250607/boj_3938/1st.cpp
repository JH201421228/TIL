#include <iostream>
#include <vector>
#include <queue>
using namespace std;


struct Edge {
    int x, c, d, inv;
    Edge() = default;
    Edge(int x, int c, int d, int inv) : x(x), c(c), d(d), inv(inv) {};
};

int src = 366<<1, sink = 366<<1|1, ans, N;
int pre[367<<1], dist[367<<1], indx[367<<1], checker[367<<1];
vector<Edge> G[367<<1];

void set_edge(int u, int v, int c, int d) {
    G[u].emplace_back(v, c, -d, G[v].size());
    G[v].emplace_back(u, 0, d, G[u].size()-1);

    return;
}

int spfa() {
    ans = 0;

    while (true) {
        fill(pre, pre+sink+1, -1); fill(dist, dist+sink+1, 1e9); fill(indx, indx+sink+1, -1); fill(checker, checker+sink+1, 0);
        queue<int> q; q.push(src); dist[src] = 0; checker[src] = 1;

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

        if (pre[sink] == -1) break;;

        for (int n = sink; n != src; n = pre[n]) {
            auto& edge = G[pre[n]][indx[n]];
            --edge.c;
            ++G[n][edge.inv].c;
        }

        ans += dist[sink];
    }

    return -ans;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    while (true) {
        cin >> N;
        if (!N) break;

        for (int idx = 0; idx < 367<<1; ++idx) G[idx].clear();
        set_edge(src, 1<<1, 2, 0);
        set_edge(365<<1|1, sink, 2, 0);
        for (int i = 1; i < 366; ++i) set_edge(i<<1, i<<1|1, 1e9, 0);
        for (int u = 1; u < 365; ++u) set_edge(u<<1|1, (u+1)<<1, 1e9, 0);
        for (int i = 0; i < N; ++i) {
            int a, b, c; cin >> a >> b >> c;
            set_edge(a<<1, b<<1|1, 1, c);
        }

        cout << spfa() << '\n';
    }

    return 0;
}