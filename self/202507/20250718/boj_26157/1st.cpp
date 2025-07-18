#include <iostream>
#include <vector>
#include <stack>
#include <queue>
using namespace std;


int N, M, O = 0, Z = 0, cmp = 1;
int F[200001], V[200001], order[200001];
vector<int> G[200001], graph[200001], ans;
stack<int> S;
queue<int> q;


int scc(int n) {
    int p = ++O;
    V[n] = O;
    S.push(n);

    for (auto& x : G[n]) {
        if (!V[x]) p = min(p, scc(x));
        else if (!F[x]) p = min(p, V[x]);
    }

    if (p == V[n]) {
        ++Z;

        while (!S.empty()) {
            int o = S.top(); S.pop();
            F[o] = Z;

            if (n == o) break;
        }
    }

    return p;
}


void generate_graph() {
    for (int n = 1; n < N+1; ++n) {
        int u = F[n];

        for (auto& x : G[n]) {
            int v = F[x];

            if (u == v) continue;

            graph[u].emplace_back(v);
            ++order[v];
        }
    }
}


void topology_sort() {
    for (int idx = 1; idx < Z+1; ++idx) {
        if (!order[idx]) q.push(idx);
    }

    if (q.size() > 1) {
        cout << 0 << '\n';
        return;
    }

    int res = q.front();
    while (!q.empty()) {
        if (q.size() > 1) {
            cout << 0 << '\n';
            return;
        }

        int n = q.front(); q.pop();
        for (auto& x : graph[n]) {
            --order[x];

            if (!order[x]) {
                q.push(x);
                ++cmp;
            }
        }
    }

    if (cmp == Z) {
        for (int idx = 1; idx < N+1; ++idx) {
            if (F[idx] == res) ans.emplace_back(idx);
        }
        
        cout << ans.size() << '\n';
        for (auto& x : ans) cout << x << ' ';
        cout << '\n';
        return;
    }
    else {
        cout << 0 << '\n';
        return;
    }
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> N >> M;

    for (int i = 0; i < M; ++i) {
        int u, v; cin >> u >> v;
        G[u].emplace_back(v);
    }

    for (int n = 1; n < N+1; ++n) {
        if (!V[n]) scc(n);
    }

    generate_graph();

    topology_sort();

    return 0;
}