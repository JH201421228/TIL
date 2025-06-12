#include <iostream>
#include <vector>
#include <queue>
using namespace std;


struct Edge{
    int x, c, d, inv;
    Edge() = default;
    Edge(int x, int c, int d, int inv) : x(x), c(c), d(d), inv(inv) {};
};

int src = 101<<1, sink = 101<<1|1, cur = 0, tar = 0, ans = 0, N, X, Y, Z;
int pre[102<<1], dist[102<<1], indx[102<<1], checker[102<<1];
vector<Edge> G[102<<1];

void set_edge(int u, int v, int c, int d) {
    G[u].emplace_back(v, c, d, G[v].size());
    G[v].emplace_back(u, 0, -d, G[u].size()-1);

    return;
}

int solve() {
    while (true) {
        fill(pre, pre+sink+1, -1); fill(indx, indx+sink+1, -1); fill(checker, checker+sink+1, 0); fill(dist, dist+sink+1, 1e9);
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
    
    return ans;
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    
    cin >> N >> X >> Y >> Z;

    for (int i = 1; i < N+1; ++i) {
        int a, b; cin >> a >> b;
        cur += a; tar += b;
        set_edge(src, i<<1, a, 0);
        set_edge(i<<1|1, sink, b, 0);
    }

    if (tar > cur) ans += (tar-cur)*X;
    else ans += (cur-tar)*Y;

    int fee = X+Y;
    for (int u = 1; u < N+1; ++u) {
        for (int v = 1; v < N+1; ++v) {
            int base = abs(u-v)*Z;
            int charge = min(fee, base);
            set_edge(u<<1, v<<1|1, 1e9, charge);
        }
    }
    
    cout << solve() << '\n';

    return 0;
}