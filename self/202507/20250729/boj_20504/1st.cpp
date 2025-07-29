#include <iostream>
#include <vector>
#include <stack>
#include <unordered_map>
using namespace std;

int N, M, O = 0, C = 0;
int V[200001], F[200001];
vector<int> G[200001];
stack<int> S;
unordered_map<int, vector<int>> parent;
unordered_map<int, bool> target_cycles;

int scc(int n) {
    int p = ++O;
    V[n] = O;
    S.push(n);

    for (auto& x : G[n]) {
        if (!V[x]) p = min(p, scc(x));
        else if (!F[x]) p = min(p, V[x]);
    }

    if (p == V[n]) {
        C += 1;
        
        while (!S.empty()) {
            int o = S.top(); S.pop();
            F[o] = C;

            if (o == n) break;
        }
    }

    return p;
}

void solve() {
    cin >> N >> M;

    for (int i = 0; i < M; ++i) {
        int u, v; cin >> u >> v;
        G[u].emplace_back(v);
    }

    for (int n = 1; n < N+1; ++n) {
        if (!V[n]) scc(n);
    }

    for (int idx = 1; idx < C+1; ++idx) {
        parent[idx] = vector<int>();
    }

    for (int n = 1; n < N+1; ++n) {
        for (auto& x : G[n]) {
            if (F[n] != F[x]) parent[F[x]].emplace_back(F[n]);
        }
    }

    for (const auto& [k, v] : parent) {
        if (v.empty()) target_cycles[k] = false;
    } 

    int Z; cin >> Z;
    for (int i = 0; i < Z; ++i) {
        int n; cin >> n;
        if (target_cycles.find(F[n]) != target_cycles.end()) target_cycles[F[n]] = true;
    }

    for (const auto& [k, v] : target_cycles) {
        if (!v) {
            cout << -1 << '\n';
            return;
        }
    }

    cout << target_cycles.size() << '\n';

    return;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    solve();

    return 0;
}