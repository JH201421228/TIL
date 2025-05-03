#include <iostream>
#include <vector>
#include <queue>
using namespace std;

struct Edge {
    int x, c, d, inv;
    Edge() = default;
    Edge(int x, int c, int d, int inv): x(x), c(c), d(d), inv(inv) {};
};

int delta[2][2] = {{1, 0}, {0, 1}};
int N, K, src, sink, ans, pre[5002], dist[5002], checker[5002], indx[5002], maze[50][50];
vector<Edge> G[5002];

void set_edge(int u, int v, int c, int d) {
    G[u].emplace_back(v, c, -d, G[v].size());
    G[v].emplace_back(u, 0, d, G[u].size()-1);

    return;
}

int solve() {
    fill(pre, pre+5002, -1); fill(indx, indx+5002, -1); fill(dist, dist+5002, 1e9); fill(checker, checker+5002, 0);
    queue<int> q; q.push(src); dist[src] = 0; checker[src] = 1;

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

    if (dist[sink] == 1e9) return 0;

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

    cin >> N >> K;

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            cin >> maze[i][j];
        }
    }

    src = 2; sink = (N*N)<<1|1;

    for (int n = 1; n < N*N+1; ++n) {
        set_edge(n<<1, n<<1|1, 1, maze[int((n-1)/N)][(n-1)%N]);
        set_edge(n<<1, n<<1|1, 1e9, 0);
    }

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            int u = N*i+j+1;
            for (auto& dd : delta) {
                int ii = i+dd[0]; int jj = j+dd[1];
                if (ii >= 0 && ii < N && jj >= 0 && jj < N) {
                    int v = N*ii+jj+1;
                    set_edge(u<<1|1, v<<1, 1e9, 0);
                }
            }
        }
    }

    ans = 0;

    while (K--) {
        ans += solve();
    }

    cout << -ans << '\n';

    return 0;
}