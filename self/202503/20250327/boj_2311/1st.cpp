#include <iostream>
#include <vector>
#include <queue>
using namespace std;


int N, M, C[2001][2001], F[2001][2001], D[2001][2001], pre[2001], dist[2001], checker[2001], ans = 0;
vector<int> G[2001];

void setVertex(int n) {
    G[n].emplace_back(n+N);
    G[n+N].emplace_back(n);
    C[n][n+N] = (1<<30)-1;
}

void setEgde(int u, int v, int c) {
    setVertex(u); setVertex(v);
    G[u+N].emplace_back(v); G[v].emplace_back(u+N); C[u+N][v] = 1; D[u+N][v] = c; D[v][u+N] = -c;
    G[v+N].emplace_back(u); G[u].emplace_back(v+N); C[v+N][u] = 1; D[v+N][u] = c; D[u][v+N] = -c;
}

void solve() {
    for (int z = 0; z < 2; ++z) {
        fill(pre, pre+2*N+1, -1); fill(dist, dist+2*N+1, (1<<30)-1); fill(checker, checker+2*N+1, 0);
        queue<int> q;
        q.push(1); checker[1] = 1; dist[1] = 0;

        while (!q.empty()) {
            int n = q.front(); q.pop(); checker[n] = 0;

            for (auto& x : G[n]) {
                if (C[n][x] > F[n][x] && dist[x] > dist[n] + D[n][x]) {
                    dist[x] = dist[n] + D[n][x]; pre[x] = n;

                    if (!checker[x]) {
                        q.push(x); checker[x] = 1;
                    }
                }
            }
        }
        
        for (int n = 2*N; n != 1; n = pre[n]) {
            ++F[pre[n]][n]; --F[n][pre[n]]; ans += D[pre[n]][n];
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> N >> M;

    for (int n = 1; n < N+1; ++n) setVertex(n);

    for (int i = 0; i < M; ++i) {
        int a, b, c; cin >> a >> b >> c;
        setEgde(a, b, c);
    }

    solve();

    cout << ans << '\n';

    return 0;
}