#include <iostream>
#include <vector>
using namespace std;

vector<vector<int>> G;
int V[200001] = {};
int F[200001] = {};
vector<int> S;
int O = 0;
int cnt = 0;

int scc(int n) {
    int p = V[n] = ++O;
    S.emplace_back(n);

    for (auto& x : G[n]) {
        if (!V[x]) {
            p = min(p, scc(x));
        }
        else if (!F[x]) {
            p = min(p, V[x]);
        }
    }

    if (p == V[n]) {
        ++cnt;

        while (!S.empty()) {
            int out = S.back();
            S.pop_back();
            F[out] = cnt;

            if (out == n) {
                break;
            }
        }
    }

    return p;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int N, M; cin >> N >> M;

    for (int i = 0; i < N+1; ++i) {
        G.emplace_back(vector<int>());
    }

    for (int i = 0; i < M; ++i) {
        int u, v; cin >> u >> v;
        G[u].emplace_back(v);
    }

    for (int i = 1; i < N+1; ++i) {
        if (!V[i]) {
            scc(i);
        }
    }

    if (cnt == 1) {
        cout << "Yes" << "\n";
    }
    else {
        cout << "No" << "\n";
    }
}