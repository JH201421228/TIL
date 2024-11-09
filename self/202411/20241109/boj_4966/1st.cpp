#include <iostream>
#include <vector>
using namespace std;

int M, N;
int r[501], b[501], V[501], C[501];
vector<int> G[501];

bool is_disjoint(int a, int b) {
    if (b == 1) {
        return false;
    }

    if (a % b) {
        return is_disjoint(b, a % b);
    }
    else {
        return true;
    }
}

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

    while (true) {
        cin >> M >> N;

        if (!N && !M) {
            break;
        }

        for (int i = 1; i < M+1; ++i) {
            cin >> b[i];
            G[i].clear();
        }

        for (int i = 1; i < N+1; ++i) {
            cin >> r[i];
            C[i] = 0;
        }

        for (int i = 1; i < M+1; ++i) {
            int a = b[i];
            for (int j = 1; j < N+1; ++j) {
                int b = r[j];

                if (is_disjoint(max(a, b), min(a, b))) {
                    G[i].emplace_back(j);
                }
            }
        }

        int ans = 0;
        for (int i = 1; i < M+1; ++i) {
            for (int j = 1; j < N+1; ++j) {
                V[j] = 0;
            }
            
            if (B(i)) {
                ++ans;
            }
        }

        cout << ans << '\n';
    }

    return 0;
}