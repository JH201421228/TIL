#include <iostream>
#include <vector>
#include <stack>
using namespace std;

int D, L, O = 0, ans = 0;
int V[5001], F[5001];
vector<int> G[5001];
stack<int> S;

int scc(int n) {
    int p = ++O;
    V[n] = O;
    S.push(n);

    for (int& x : G[n]) {
        if (!V[x]) p = min(p, scc(x));
        else if (!F[x]) p = min(p, V[x]);
    }

    if (V[n] == p) {
        int tmp = 0;

        while (!S.empty()) {
            int o = S.top(); S.pop();
            tmp += 1;

            F[o] = 1;

            if (o == n) break;
        }

        ans = max(ans, tmp);
    }

    return p;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> D >> L;

    for (int i = 0; i < L; ++i) {
        int u, v; cin >> u >> v;
        G[u].emplace_back(v);
    }

    for (int n = 1; n < D+1; ++n) {
        if (!V[n]) scc(n);
    }

    cout << ans << '\n';

    return 0;
}