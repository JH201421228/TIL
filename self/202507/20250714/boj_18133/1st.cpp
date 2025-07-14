#include <iostream>
#include <queue>
#include <stack>
#include <vector>
#include <unordered_map>
#include <set>
using namespace std;


int N, M, O, cnt, V[100001], F[100001];
vector<int> G[100001];
stack<int> S;
unordered_map<int, vector<int>> connection;
set<int> uniques;


int scc(int n) {
    int p = ++O;
    V[n] = O;
    S.push(n);

    for (auto& x : G[n]) {
        if (!V[x]) p = min(p, scc(x));
        else if (!F[x]) p = min(p, V[x]);
    }

    if (p == V[n]) {
        ++cnt;

        while (!S.empty()) {
            int o = S.top(); S.pop();
            F[o] = cnt;

            if (o == n) break;
        }
    }

    return p;
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> N >> M;
    O = 0;
    cnt = 0;

    for (int i = 0; i < M; ++i) {
        int u, v; cin >> u >> v;
        G[u].emplace_back(v);
    }

    for (int n = 1; n < N+1; ++n) {
        if (!V[n]) scc(n);
    }

    for (int idx = 1; idx < N+1; ++idx) {
        uniques.insert(F[idx]);
    }

    for (auto& n : uniques) connection[n] = vector<int>();

    for (int n = 1; n < N+1; ++n) {
        for (auto& x : G[n]) {
            if (F[x] != F[n]) connection[F[x]].emplace_back(F[n]);
        }
    }

    int ans = 0;
    for (auto& [k, v] : connection) {
        if (v.empty()) ++ans;
    }

    cout << ans << '\n';

    return 0;
}