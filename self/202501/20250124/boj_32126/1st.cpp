#include <iostream>
#include <vector>
using namespace std;


int N, K, M[400][800], C[401], V[401];
vector<int> G[801];

bool B(int n) {
    for (int x : G[n]) {
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

    cin >> N >> K;

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < K; ++j) {
            cin >> M[i][j];
        }
    }

    for (int t = 0; t < K; ++t) {
        for (int d = 0; d < N; ++d) {
            if (M[d][K-t-1]) {
                G[t+1].emplace_back(d+1);
            }
        }
    }

    int ans = 0;
    int camera = 0;
    for (int i = 1; i < K+1; ++i) {
        fill(V+1, V+N+1, 0);
        if (B(i)) {
            if (ans-camera+2 > K+1-i) {
                cout << ans << '\n';
                exit(0);
            }
            ++ans;
        }
        else {
            if (camera < ans) {
                ++camera;
            }
        }
    }
    
    cout << ans << '\n';

    return 0;
}