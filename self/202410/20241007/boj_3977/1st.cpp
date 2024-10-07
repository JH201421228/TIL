#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int O;
int GN;
int V[100000] = {};
int F[100000] = {};
int P[100000] = {};
vector<int> G[100000];
vector<int> S;
vector<int> C;

int find_scc(int n) {
    ++O;
    int p = V[n] = O;
    S.emplace_back(n);

    for (auto& x: G[n]) {
        if (V[x] == -1) {
            p = min(p, find_scc(x));
        }
        else if (!F[x]) {
            p = min(p, V[x]);
        }
    }

    if (p == V[n]) {
        ++GN;
        while (!S.empty()) {
            int out = S.back();
            S.pop_back();
            F[out] = GN;

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

    int T; cin >> T;

    for (int i = 0; i < T; ++i) {
        int N, M; cin >> N >> M;

        fill(V, V+N, -1);
        fill(F, F+N, 0);
        fill(P, P+N, 0);
        C.clear();
        for (int j = 0; j < N; ++j) {
            G[j].clear();
        }

        for (int j = 0; j < M; ++j) {
            int a, b; cin >> a >> b; G[a].emplace_back(b);
        }

        O = 0;
        GN = 0;

        for (int j = 0; j < N; ++j) {
            if (V[j] == -1) {
                find_scc(j);
            }
        }

        for (int j = 0; j < N; ++j) {
            for (auto& k: G[j]) {
                if (F[j] != F[k]) {
                    P[F[k]] = F[j];
                }
            }
        }

        for (int j = 1; j < GN+1; ++j) {
            if (!P[j]) {
                C.emplace_back(j);
            }
        }

        if (C.size() > 1) {
            cout << "Confused" << "\n";
        }
        else {
            if (!C.empty()) {
                for (int j = 0; j < N; ++j) {
                    if (C[0] == F[j]) {
                        cout << j << "\n";
                    }
                }
            }
        }
        cout << "\n";
    }

    return 0;
}