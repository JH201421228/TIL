#include <iostream>
#include <vector>
using namespace std;

int T, M, N, C[201], V[201], ans;
vector<int> G[201];

bool B(int n) {
    for (int x : G[n]) {
        if (V[x]) continue;
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

    cin >> T;

    for (int z = 0; z < T; ++z) {
        cout << "Data Set " << z+1 << ":" << '\n';
        cin >> M >> N;

        for (int idx = 1; idx < N+1; ++idx) G[idx].clear();
        
        for (int i = 0; i < N; ++i) {
            int t; cin >> t;
            for (int j = 0; j < t; ++j) {
                int tmp; cin >> tmp;
                G[i+1].emplace_back(tmp);
            }
        }

        ans = 0;
        fill(C, C+M+1, 0);

        for (int n = 1; n < N+1; ++n) {
            fill(V, V+M+1, 0);
            if (B(n)) ++ans;
        }

        cout << ans << "\n\n";
    }

    return 0;
}