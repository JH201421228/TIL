#include <iostream>
#include <vector>
using namespace std;

int N, M, z;
int T[100001];
int A[100001];
int E[100001];
vector<int> G[100001];
int cnt = 0;

void dfs(int n) {
    A[n] = ++cnt;
    for (auto& x : G[n]) {
        dfs(x);
    }
    E[n] = cnt;
}

void U(int idx, int v) {
    while (idx < N+1) {
        T[idx] += v;
        idx += (idx & -idx);
    }
}

int S(int idx) {
    int res = 0;
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

    cin >> N >> M;

    cin >> z;
    for (int i = 2; i < N+1; ++i) {
        int a; cin >> a;
        G[a].emplace_back(i);
    }

    dfs(1);

    for (int i = 0; i < M; ++i) {
        int a; cin >> a;

        if (a == 1) {
            int b, c; cin >> b >> c;
            U(A[b], c);
        }
        else {
            int b; cin >> b;
            cout << S(E[b]) - S(A[b]-1) << "\n";
        }
    }

    return 0;
}