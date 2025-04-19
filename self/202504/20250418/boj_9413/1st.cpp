#include <iostream>
#include <vector>
#include <queue>
using namespace std;

static int T, N, M, ans, src = 601, sink = 602, C[603][603], D[603][603], F[603][603], pre[603], dist[603], checker[603];
static vector<int> G[603];

static void set_edge(int u, int v) {
    G[u].emplace_back(v); G[v].emplace_back(u); C[u][v] = 1;
    return;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> T;

    for (int z = 0; z < T; ++z) {
        ans = 0;

        cin >> N >> M;
        fill(&C[0][0], &C[0][0]+606*603, 0); fill(&D[0][0], &D[0][0]+603*603, 0); fill(&F[0][0], &F[0][0]+603*603, 0);

        for (int i = 1; i < N+1; ++i) {
            set_edge(i, i+N); set_edge(src, i); set_edge(i+N, sink); D[i][i+N] = -1; D[i+N][i] = 1;
        }

        for (int i = 0; i < M; ++i) {
            int u, v; cin >> u >> v; set_edge(u+N, v);
        }

        for (int i = 0; i < 2; ++i) {
            fill(pre, pre+603, -1); fill(dist, dist+603, 1e9); fill(checker, checker+603, 0);
            queue<int> q; q.push(src); dist[src] = 0; checker[src] = 1;

            while (!q.empty()) {
                int n = q.front(); q.pop(); checker[n] = 0;

                for (auto& x : G[n]) {
                    if (C[n][x] > F[n][x] && dist[x] > dist[n] + D[n][x]) {
                        pre[x] = n; dist[x] = dist[n] + D[n][x];

                        if (!checker[x]) {
                            checker[x] = 1; q.push(x);
                        }
                    }
                }
            }

            if (pre[sink] == -1) break;

            for (int n = sink; n != src; n = pre[n]) {
                F[pre[n]][n]++; F[n][pre[n]]--; ans += D[pre[n]][n];
            }
        }

        cout << -ans << '\n';
    }

    return 0;
}