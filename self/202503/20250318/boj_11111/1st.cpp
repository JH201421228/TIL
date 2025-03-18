#include <iostream>
#include <vector>
#include <queue>
#include <unordered_map>
using namespace std;


int ans = 0, N, M, src = 2501, sink = 2502, D[2503][2503], F[2503][2503], C[2503][2503], pre[2503], dist[2503], checker[2503], maxv = (1<<31)-1, grades[5][5] = {{10, 8, 7, 5, 1}, {8, 6, 4, 3, 1}, {7, 4, 3, 2, 1}, {5, 3, 2, 2, 1}, {1, 1, 1, 1, 0}}, delta[4][2] = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
char B[50][50];
vector<int> G[2503];
queue<int> q;
unordered_map<char, int> T = {{'A', 0}, {'B', 1}, {'C', 2}, {'D', 3}, {'F', 4}};

int main () {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> N >> M;

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            cin >> B[i][j];
        }
    }

    for (int i = 0; i < N; ++i) {
        for (int j = (i+1)%2; j < M; j+=2) {
            int v = i*M+j+1;
            G[v].emplace_back(sink); G[sink].emplace_back(v);
            C[v][sink] = 1;
        }

        for (int j = i%2; j < M; j+=2) {
            int u = i*M+j+1;
            G[src].emplace_back(u); G[u].emplace_back(src);
            G[u].emplace_back(sink); G[sink].emplace_back(u);
            C[u][sink] = 1; C[src][u] = 1;

            for (auto& [di, dj] : delta) {
                int xi = i+di, xj = j+dj;
                if (xi >= 0 && xi < N && xj >= 0 && xj < M) {
                    int v = xi*M+xj+1;
                    G[u].emplace_back(v); G[v].emplace_back(u);
                    C[u][v] = 1;
                    D[u][v] = -grades[T[B[i][j]]][T[B[xi][xj]]]; D[v][u] = -D[u][v];
                }
            }
        }
    }

    while (true) {
        fill(pre, pre+2503, -1); fill(dist, dist+2503, maxv); fill(checker, checker+2503, 0);
        q = queue<int>(); q.push(src);
        checker[src] = 1; dist[src] = 0;

        while (!q.empty()) {
            int n = q.front(); q.pop();
            checker[n] = 0;

            for (auto& x : G[n]) {
                if (C[n][x] > F[n][x] && dist[x] > dist[n] + D[n][x]) {
                    dist[x] = dist[n] + D[n][x];
                    pre[x] = n;

                    if (!checker[x]) {
                        checker[x] = 1;
                        q.push(x);
                    }
                }
            }
        }

        if (pre[sink] == -1) break;

        for (int n = sink; n != src; n = pre[n]) {
            F[pre[n]][n] += 1; F[n][pre[n]] -= 1;
            ans += D[pre[n]][n];
        }
    }

    cout << -ans << '\n';

    return 0;
}