#include <iostream>
#include <vector>
using namespace std;

int N, C, M;
vector<int> G[200001];
int A[200001];
int E[200001];
int W[200001];
long long T[200001];
int cnt = 0;
int order = 0;

void dfs(int n) {
    A[n] = ++cnt;
    W[n] = ++order;
    for (auto& x : G[n]) {
        if (A[x] == 0) {
            dfs(x);
            --order;
        }
    }
    E[n] = cnt;
}

void U(int idx) {
    while (idx < N+1) {
        T[idx] += 1;
        idx += (idx & -idx);
    }
}

long long S(int idx) {
    long long res = 0;
    while (idx > 0) {
        res += T[idx];
        idx -= (idx & -idx);
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> N >> C;

    for (int i = 0; i < N-1; ++i) {
        int u, v; cin >> u >> v;
        G[u].emplace_back(v);
        G[v].emplace_back(u);
    }

    dfs(C);

    cin >> M;
    for (int i = 0; i < M; ++i) {
        int a, b; cin >> a >> b;

        if (a == 1) {
            U(A[b]);
        }
        else {
            cout << W[b]*(S(E[b])-S(A[b]-1)) << '\n';
        }
    }

    return 0;
}