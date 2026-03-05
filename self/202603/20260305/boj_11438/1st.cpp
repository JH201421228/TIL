#include <iostream>
#include <vector>
using namespace std;


int N, M;
int V[100'001];
int D[100'001];
int A[100'001][18];
vector<int> G[100'001];


void dfs(int cur, int depth) {
    D[cur] = depth;

    for (auto& x : G[cur]) {
        if (!V[x]) {
            V[x] = 1;
            A[x][0] = cur;

            dfs(x, depth+1);
        }
    }

    return;
}


int LCA(int a, int b) {
    if (D[a] < D[b]) swap(a, b);

    if (D[a] != D[b]) {
        int diff = D[a] - D[b];

        for (int i = 0; i < 18; ++i) {
            if (diff & (1<<i)) a = A[a][i];
        }
    }
    
    if (a == b) return a;
    
    for (int i = 17; i >= 0; --i) {
        if (A[a][i] != A[b][i]) {
            a = A[a][i];
            b = A[b][i];
        }
    }

    return A[a][0];
}


void solve() {
    cin >> N;

    for (int i = 0; i < N-1; ++i) {
        int u, v; cin >> u >> v;
        G[u].emplace_back(v);
        G[v].emplace_back(u);
    }

    V[1] = 1;

    dfs(1, 0);

    for (int i = 1; i < 18; ++i) {
        for (int j = 1; j < N+1; ++j) {
            A[j][i] = A[A[j][i-1]][i-1];
        }
    }

    cin >> M;

    for (int i = 0; i < M; ++i) {
        int q1, q2; cin >> q1 >> q2;
        cout << LCA(q1, q2) << '\n';
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