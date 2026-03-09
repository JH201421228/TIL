#include <iostream>
#include <vector>
using namespace std;


int N, K;
int D[100'001];
int V[100'001];
int A[100'001][18][3];
vector<pair<int, int>> G[100'001];


void dfs(int cur, int depth) {
    D[cur] = depth;

    for (auto& x : G[cur]) {
        int nxt = x.first;
        int cost = x.second;

        if (!V[nxt]) {
            V[nxt] = 1;
            A[nxt][0][0] = cur;
            A[nxt][0][1] = cost;
            A[nxt][0][2] = cost;

            dfs(nxt, depth+1);
        }
    }

    return;
}


pair<int, int> LCA(int a, int b) {
    if (D[a] < D[b]) swap(a, b);

    int min_res = INT32_MAX;
    int max_res = INT32_MIN;

    if (D[a] != D[b]) {
        int diff = D[a] - D[b];
        for (int i = 0; i < 18; ++i) {
            if (diff & (1<<i)) {
                max_res = max(max_res, A[a][i][1]);
                min_res = min(min_res, A[a][i][2]);
                a = A[a][i][0];
            }
        }
    }

    if (a == b) {
        if (min_res == INT32_MAX) min_res = 0;
        if (max_res == INT32_MIN) max_res = 0;

        return {min_res, max_res};
    }

    for (int i = 17; i >= 0; --i) {
        if (A[a][i][0] != A[b][i][0]) {
            max_res = max(max_res, max(A[a][i][1], A[b][i][1]));
            min_res = min(min_res, min(A[a][i][2], A[b][i][2]));
            a = A[a][i][0];
            b = A[b][i][0];
        }
    }

    max_res = max(max_res, max(A[a][0][1], A[b][0][1]));
    min_res = min(min_res, min(A[a][0][2], A[b][0][2]));

    if (min_res == INT32_MAX) min_res = 0;
    if (max_res == INT32_MIN) max_res = 0;

    return {min_res, max_res};
}


void solve() {
    cin >> N;
    for (int idx = 0; idx < N+1; ++idx) {
        for (int jdx = 0; jdx < 18; ++jdx) {
            A[idx][jdx][1] = INT32_MIN;
            A[idx][jdx][2] = INT32_MAX;
        }
    }

    for (int i = 0; i < N-1; ++i) {
        int u, v, c; cin >> u >> v >> c;
        G[u].emplace_back(make_pair(v, c));
        G[v].emplace_back(make_pair(u, c));
    }

    V[1] = 1;
    dfs(1, 0);

    for (int i = 1; i < 18; ++i) {
        for (int j = 1; j < N+1; ++j) {
            A[j][i][0] = A[A[j][i-1][0]][i-1][0];
            A[j][i][1] = max(A[A[j][i-1][0]][i-1][1], A[j][i-1][1]);
            A[j][i][2] = min(A[A[j][i-1][0]][i-1][2], A[j][i-1][2]);
        }
    }

    cin >> K;

    for (int i = 0; i < K; ++i) {
        int u, v; cin >> u >> v;
        auto res = LCA(u, v);
        cout << res.first << " " << res.second << '\n';
    }

    return;
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    solve();

    return 0;
}