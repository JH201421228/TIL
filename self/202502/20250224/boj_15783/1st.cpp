#include <iostream>
#include <vector>
#include <stack>
#include <unordered_map>
#include <unordered_set>
using namespace std;

int N, M, O = 0, V[100001], F[100001], ans;
vector<int> G[100001];
stack<int> S;
unordered_map<int, unordered_set<int>> checker;

int scc(int n) {
    int p = ++O;
    V[n] = O;
    S.push(n);

    for (auto& x : G[n]) {
        if (!V[x]) {
            p = min(p, scc(x));
        }
        else if (!F[x]) {
            p = min(p, V[x]);
        }
    }

    if (p == V[n]) {
        while (!S.empty()) {
            int o = S.top(); S.pop();
            F[o] = p;
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

    for (int i = 0; i < M; ++i) {
        int u, v; cin >> u >> v;

        G[u+1].emplace_back(v+1);
    }

    for (int n = 1; n < N+1; ++n) {
        if (!V[n]) scc(n);
    }

    for (int i = 1; i < N+1; ++i) {
        checker[F[i]] = unordered_set<int>();
    }

    for (int s = 1; s < N+1; ++s) {
        for (auto& e : G[s]) {
            if (F[s] != F[e]) {
                checker[F[e]].insert(F[s]);
            }
        }
    }

    for (const auto& [k, v] : checker) {
        if (v.empty()) {
            ++ans;
        }
    }

    cout << ans << '\n';

    return 0;
}