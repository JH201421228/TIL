#include <iostream>
#include <vector>
using namespace std;


int N, M;
int V[100'001];
int D[100'001];
long long A[100'001][18][2];
vector<pair<int, int>> G[100'001];


void dfs(int cur, int depth) {
    D[cur] = depth;

    for (auto& nxt : G[cur]) {
        int x = nxt.first;
        int c = nxt.second;

        if (!V[x]) {
            V[x] = 1;
            A[x][0][0] = cur;
            A[x][0][1] = c;

            dfs(x, depth+1);
        }
    }

    return;
}


pair<long long, long long> LCA(int a, int b) {
    if (D[a] < D[b]) swap(a, b);

    long long cost = 0;

    if (D[a] != D[b]) {
        int diff = D[a] - D[b];

        for (int i = 0; i < 18; ++i) {
            if ((diff & (1<<i)) > 0) {
                cost += A[a][i][1];
                a = A[a][i][0];
            }
        }
    }

    if (a == b) return {cost, a};

    for (int i = 17; i > -1; --i) {
        if (A[a][i][0] != A[b][i][0]) {
            cost += A[a][i][1];
            cost += A[b][i][1];

            a = A[a][i][0];
            b = A[b][i][0];
        }
    }

    cost += A[a][0][1];
    cost += A[b][0][1];

    return {cost, A[a][0][0]};
}


void solve() {
    cin >> N;

    for (int i = 0; i < N-1; ++i) {
        int u, v, w; cin >> u >> v >> w;
        G[u].emplace_back(make_pair(v, w));
        G[v].emplace_back(make_pair(u, w));
    }

    V[1] = 1;
    dfs(1, 0);

    for (int i = 1; i < 18; ++i) {
        for (int j = 0; j < N+1; ++j) {
            A[j][i][0] = A[A[j][i-1][0]][i-1][0];
            A[j][i][1] = A[j][i-1][1] + A[A[j][i-1][0]][i-1][1];
        }
    }

    cin >> M;

    for (int i = 0; i < M; ++i) {
        int flag; cin >> flag;
        
        int u, v; cin >> u >> v;
        
        auto res = LCA(u, v);

        if (flag == 1) cout << res.first << '\n';
        else {
            int k; cin >> k; --k;

            long long node = res.second;

            if (D[u] - D[node] < k) {
                k = D[u] + D[v] - 2*D[node] - k;
                u = v;
            }

            for (int i = 17; i > -1; --i) {
                if ((k & (1<<i)) > 0) u = A[u][i][0];
            }

            cout << u << '\n';
        }
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