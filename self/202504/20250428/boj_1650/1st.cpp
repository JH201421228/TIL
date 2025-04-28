#include <iostream>
#include <vector>
#include <queue>
using namespace std;


struct Edge {
    int x, c, d, inv;
    Edge() = default;
    Edge(int x, int c, int d, int inv) : x(x), c(c), d(d), inv(inv) {};
};

int N, M, pre[2002], dist[2002], checker[2002], indx[2002], src, sink, ans = 0;
vector<Edge> G[2002];

void set_edge(int u, int v, int c, int d) {
    G[u].emplace_back(v, c, d, G[v].size());
    G[v].emplace_back(u, 0, -d, G[u].size()-1);
}

int solve() {
    fill(pre, pre+2002, -1); fill(dist, dist+2002, 1e9); fill(indx, indx+2002, -1); fill(checker, checker+2002, 0);
    queue<int> q; q.push(src); checker[src] = 1; dist[src] = 0;
    
    while (!q.empty()) {
        int n = q.front(); q.pop(); checker[n] = 0;
        
        for (int idx = 0; idx < G[n].size(); idx++) {
            auto& edge = G[n][idx];
            if (edge.c && dist[edge.x] > dist[n] + edge.d) {
                dist[edge.x] = dist[n] + edge.d;
                pre[edge.x] = n; indx[edge.x] = idx;
                
                if (!checker[edge.x]) {
                    checker[edge.x] = 1; q.push(edge.x);
                }
            }
        }
    }
    
    for (int n = sink; n != src; n = pre[n]) {
        --G[pre[n]][indx[n]].c; ++G[n][G[pre[n]][indx[n]].inv].c;
    }
    
    return dist[sink];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    
    cin >> N >> M;
    src = 2; sink = (N<<1)|1;
    
    for (int n = 1; n < N+1; ++n) set_edge(n<<1, (n<<1)|1, 1e9, 0);
    
    for (int i = 0; i < M; ++i) {
        int u, v, d; cin >> u >> v >> d;
        set_edge((u<<1)|1, v<<1, 1, d); set_edge((v<<1)|1, u<<1, 1, d);
    }

    for (int i = 0; i < 2; ++i) ans += solve();

    cout << ans << '\n';

    return 0;
}