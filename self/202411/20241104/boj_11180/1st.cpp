#include <iostream>
#include <vector>
using namespace std;

int N, M;
int V[1001], C[1001];
vector<int> G[1001];

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

    cin >> N >> M;

    for (int i = 0; i < M; ++i) {
        int a, b; cin >> a >> b;
        G[a].emplace_back(b);
        G[b].emplace_back(a);
    }

    for (int i = 1; i < N+1; ++i) {
        for (int j = 1; j < N+1; ++j) {
            V[j] = 0;
        }
        if (!B(i)) {
            cout << "Impossible" << '\n';
            exit(0);
        }
    }

    for (int i = 1; i < N+1; ++i) {
        cout << C[i] << '\n';
    }

    return 0;
}