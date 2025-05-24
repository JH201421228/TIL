#include <iostream>
#include <vector>
#include <tuple>
#include <queue>
#include <algorithm>
#include <climits>
using namespace std;

struct Edge {
    int x, c, d, inv;
    Edge(int x, int c, int d, int inv) : x(x), c(c), d(d), inv(inv) {}
};

vector<Edge> G[610];
int N;
int src, sink;
int A[300], H[300], L[300];
vector<tuple<int, int, int>> arr;

void set_edge(int u, int v, int c, int d) {
    G[u].emplace_back(v, c, d, G[v].size());
    G[v].emplace_back(u, 0, -d, G[u].size() - 1);
}

void solve() {
    int ans = 0;

    while (true) {
        vector<int> pre(sink + 1, -1), dist(sink + 1, INT_MAX), indx(sink + 1, -1), checker(sink + 1, 0);
        queue<int> q;

        dist[src] = 0;
        checker[src] = 1;
        q.push(src);

        while (!q.empty()) {
            int n = q.front(); q.pop();
            checker[n] = 0;

            for (int i = 0; i < G[n].size(); ++i) {
                Edge &e = G[n][i];

                if (e.c && dist[e.x] > dist[n] + e.d) {
                    dist[e.x] = dist[n] + e.d;
                    pre[e.x] = n;
                    indx[e.x] = i;

                    if (!checker[e.x]) {
                        checker[e.x] = 1;
                        q.push(e.x);
                    }
                }
            }
        }

        if (pre[sink] == -1) break;

        for (int n = sink; n != src; n = pre[n]) {
            Edge &e = G[pre[n]][indx[n]];
            e.c--;
            G[n][e.inv].c++;
        }

        ans += dist[sink];
    }

    cout << -ans << '\n';
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> N;

    for (int i = 0; i < N; ++i) cin >> A[i];
    for (int i = 0; i < N; ++i) cin >> H[i];
    for (int i = 0; i < N; ++i) cin >> L[i];

    for (int i = 0; i < N; ++i)
        arr.emplace_back(A[i], H[i], L[i]);

    sort(arr.rbegin(), arr.rend());  // 역순 정렬 (내림차순)

    src = 2 * N + 2;
    sink = 2 * N + 3;

    // source to left split
    set_edge(src, 1 << 1, get<2>(arr[0]), get<1>(arr[0]));
    for (int v = 2; v <= N; ++v)
        set_edge(src, v << 1, get<2>(arr[v - 1]) - 1, get<1>(arr[v - 1]));

    // right split to sink
    for (int u = 2; u <= N; ++u)
        set_edge(u << 1 | 1, sink, 1, get<1>(arr[u - 1]));

    // left to right split (XOR edge)
    for (int u = 1; u <= N; ++u) {
        for (int v = u + 1; v <= N; ++v) {
            int cost = -(get<0>(arr[u - 1]) ^ get<0>(arr[v - 1]));
            set_edge(u << 1, v << 1 | 1, 1, cost);
        }
    }

    solve();
    return 0;
}
