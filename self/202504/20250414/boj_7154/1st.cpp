#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

int satisfaction[3][4] = {{4, 3, 2, 1}, {8, 7, 6, 5}, {12, 11, 10, 9}};
int N, M, ans, src, sink, C[211][211], F[211][211], D[211][211], pre[211], dist[211], checker[211];
vector<int> G[211];

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

            int temp[4]; for (int idx = 0; idx < 5; ++idx) cin >> temp[idx];
            for (int idx = 1; idx < 5; ++idx) {
                int v = temp[idx]+1+M;
                G[u].emplace_back(v); G[v].emplace_back(u);
                D[u][v] = -satisfaction[temp[0]-1][idx-1]; D[v][u] = satisfaction[temp[0]-1][idx-1];
                C[u][v] = 1;
            }
        }

        while (true) {
            
        }
    }

    // cout << satisfaction[1][3] << '\n';

    return 0;
}