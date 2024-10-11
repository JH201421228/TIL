#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int C[100] = {};
int G[100][100];
int V[100];
int F[100] = {};
vector<vector<int>> GR;
vector<int> S;
int O = 0;
int MAX = 1000000;

int find_scc(int n, int N) {
    int p = V[n] = O = O+1;
    S.emplace_back(n);
    
    for (int i = 0; i < N; ++i) {
        if (G[n][i] == 1) {
            if (V[i] == -1) {
                p = min(p, find_scc(i, N));
            }
            else if (!F[i]) {
                p = min(p, V[i]);
            }
        }
    }

    if (p == V[n]) {
        vector<int> temp;

        while (!S.empty()) {
            int out = S.back();
            S.pop_back();
            F[out] = 1;
            temp.emplace_back(out);

            if (out == n) {
                GR.emplace_back(temp);
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

    int N; cin >> N;

    fill(V, V+N, -1);

    for (int i = 0; i < N; ++i) {
        int c; cin >> c;

        C[i] = c;
    }

    for (int i = 0; i < N; ++i) {
        string s; cin >> s;

        for (int j = 0; j < N; ++j) {
            G[i][j] = s[j] - '0';
        }
    }

    for (int i = 0; i < N; ++i) {
        if (V[i] == -1) {
            find_scc(i, N);
        }
    }

    int ans = 0;
    for (auto& gr : GR) {
        int v = MAX;
        for (auto& i : gr) {
            v = min(v, C[i]);
        }

        ans += v;
    }

    cout << ans << "\n";

    return 0;
}