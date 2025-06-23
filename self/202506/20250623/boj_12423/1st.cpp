#include <iostream>
#include <vector>
#include <queue>
using namespace std;


struct Edge {
    int x, c, d, inv;
    Edge() = default;
    Edge(int x, int c, int d, int inv) : x(x), c(c), d(d), inv(inv) {};
};

int A, B, C, D, E, F, N, T, src = 7, sink = 8;
int pre[9], dist[9], indx[9], checker[9];
int arr[3][3];
vector<Edge> G[9];

void set_edge(int u, int v, int c, int d) {
    G[u].emplace_back(v, c, d, G[v].size());
    G[v].emplace_back(u, 0, -d, G[u].size()-1);

    return;
}

int spfa() {
    int res = 0;

    while (true) {
        fill(pre, pre+9, -1); fill(indx, indx+9, -1); fill(checker, checker+9, 0); fill(dist, dist+9, 1e9);
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

        res -= flow*dist[sink];
    }

    return res;
}

int init() {
    cin >> N >> A >> B >> C >> D >> E >> F;

    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
            cin >> arr[i][j];
        }
    }

    for (int idx = 0; idx < sink+1; ++idx) G[idx].clear();

    set_edge(src, 1, A, 0); set_edge(src, 2, B, 0); set_edge(src, 3, C, 0);
    set_edge(4, sink, D, 0); set_edge(5, sink, E, 0); set_edge(6, sink, F, 0);
    
    for (int u = 0; u < 3; ++u) {
        for (int v = 0; v < 3; ++v) {
            set_edge(u+1, v+4, 1e9, -arr[u][v]);
        }
    }

    return spfa();
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> T;

    for (int t = 1; t < T+1; ++t) {
        cout << "Case #" << t << ": " << init() << '\n';
    }

    return 0;
}