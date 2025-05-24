#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <tuple>
using namespace std;


struct Edge {
    int x, c, d, inv;

    Edge() = default;
    Edge(int x, int c, int d, int inv) : x(x), c(c), d(d), inv(inv) {};
};

int src = 602, sink = 603, N, pre[604], dist[604], indx[604], checker[604], A[300], H[300], L[300], ans = 0;
vector<Edge> G[604];
vector<tuple<int, int, int>> arr;

void set_edge(int u, int v, int c, int d) {
    G[u].emplace_back(v, c, d, G[v].size());
    G[v].emplace_back(u, 0, -d, G[u].size()-1);

    return;
}

void solve() {
    while (1) {
        fill(pre, pre+sink+1, -1); fill(dist, dist+sink+1, 1e9); fill(checker, checker+sink+1, 0); fill(indx, indx+sink+1, -1);
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

        for (int n = sink; n != src; n = pre[n]) {
            auto& edge = G[pre[n]][indx[n]];
            --edge.c;
            ++G[n][edge.inv].c;
        }

        ans += dist[sink];
    }

    return;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> N;

    for (int idx = 0; idx < N; ++idx) cin >> A[idx]; 
    for (int idx = 0; idx < N; ++idx) cin >> H[idx]; 
    for (int idx = 0; idx < N; ++idx) cin >> L[idx]; 

    for (int idx = 0; idx < N; ++idx) arr.emplace_back(A[idx], H[idx], L[idx]);

    sort(arr.rbegin(), arr.rend());

    set_edge(src, 1<<1, get<2>(arr[0]), get<1>(arr[0]));
    for (int v = 2; v < N+1; ++v) set_edge(src, v<<1, get<2>(arr[v-1])-1, get<1>(arr[v-1]));
    for (int u = 2; u < N+1; ++u) set_edge(u<<1|1, sink, 1, get<1>(arr[u-1]));
    for (int u = 1; u < N+1; ++u) {
        for (int v = u+1; v < N+1; ++v) set_edge(u<<1, v<<1|1, 1, -(get<0>(arr[u-1])^get<0>(arr[v-1])));
    }

    solve();

    cout << -ans << '\n';

    return 0;
}