#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>
using namespace std;

int N, K, X, C[16], V[16];
vector<int> G[16];
vector<vector<int>> W;
stack<int> S;

bool B(int n) {
    for (auto& x : G[n]) {
        if (V[x]) {
            continue;
        }
        V[x] = 1;

        if (!C[x] || B(C[x])) {
            C[x] = n;
            return true;
        }
    }

    return false;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> N >> K >> X; W.resize(N);
    for (int i = 0; i < N; ++i) {
        int n; cin >> n; W[i].resize(n+2);
        W[i][1] = i+1;

        for (int j = 0; j < n; ++j) {
            cin >> W[i][j+2];
        }
    }

    for (int i = 0; i < N; ++i) {
        int v; cin >> v; W[i][0] = -v;
    }

    sort(W.begin(), W.end());

    for (int i = 0; i < N; ++i) {
        vector<int> l = W[i];
        for (int j = 2; j < l.size(); ++j) {
            for (int x = (l[j]-1)*X+1; x < l[j]*X+1; ++x) {
                G[i+1].emplace_back(x);
            }
        }
    }

    for (int n = 1; n < N+1; ++n) {
        fill(V, V+16, 0);
        B(n);
    }

    vector<vector<int>> ans_list;
    ans_list.resize(K);

    for (int i = 1; i < K*X+1; ++i) {
        if (C[i]) {
            ans_list[(i-1)/X].emplace_back(W[C[i]-1][1]);
        }
    }

    for (auto& ans : ans_list) {
        cout << ans.size() << ' ';
        for (auto& x : ans) {
            cout << x << ' ';
        }
        cout << '\n';
    }

    return 0;
}