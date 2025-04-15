#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

int satisfaction[3][4] = {{4, 3, 2, 1}, {8, 7, 6, 5}, {12, 11, 10, 9}};
int N, M, ans, src, sink, C[213][213], F[213][213], D[213][213], pre[213], dist[213], checker[213];
vector<int> G[213];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    while (true) {
        cin >> N >> M;
        if (!N && !M) break;

        ans = 0; src = N+M+1; sink = N+M+2;
        for (int idx = 0; idx < sink+1; ++idx) G[idx].clear();
        for (int idx = 0; idx < sink+1; ++idx) fill(C[idx], C[idx]+sink+1, 0);
        for (int idx = 0; idx < sink+1; ++idx) fill(F[idx], F[idx]+sink+1, 0);
        for (int idx = 0; idx < sink+1; ++idx) fill(D[idx], D[idx]+sink+1, 0);

        for (int i = 0; i < N; ++i) {
            int u = i+M+1;
            cin >> C[u][sink];
            G[u].emplace_back(sink); G[sink].emplace_back(u);
        }

        for (int i = 0; i < M; ++i) {
            int u = i+1;
            C[src][u] = 1;
            G[src].emplace_back(u); G[u].emplace_back(src);

            int temp[5]; for (int idx = 0; idx < 5; ++idx) cin >> temp[idx];
            for (int idx = 1; idx < 5; ++idx) {
                int v = temp[idx]+1+M;
                G[u].emplace_back(v); G[v].emplace_back(u);
                D[u][v] = -satisfaction[temp[0]-1][idx-1]; D[v][u] = satisfaction[temp[0]-1][idx-1];
                C[u][v] = 1;
            }
        }

        while (true) {
            fill(pre, pre+sink+1, -1);
            fill(dist, dist+sink+1, 1e9);
            fill(checker, checker+sink+1, 0);

            queue<int> q; q.push(src); dist[src] = 0; checker[src] = 1;

            while (!q.empty()) {
                int n = q.front(); q.pop(); checker[n] = 0;

                for (auto& x : G[n]) {
                    if (C[n][x] > F[n][x] && dist[x] > dist[n] +D[n][x]) {
                        dist[x] = dist[n] + D[n][x]; pre[x] = n;
                        if (!checker[x]) {
                            q.push(x); checker[x] = 1;
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