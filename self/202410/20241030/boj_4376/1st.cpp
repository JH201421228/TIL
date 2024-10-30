#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int N, M, S, V;
float gopers[101][2];
float holes[101][2];
vector<int> G[101];
int U[101];
int C[101];

bool B(int n) {
    for (auto& x : G[n]) {
        if (U[x]) {
            continue;
        }
        U[x] = 1;

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

    while (cin >> N >> M >> S >> V) {
        for (int i = 0; i < N; ++i) {
            cin >> gopers[i+1][0] >> gopers[i+1][1];
        }
        for (int i = 0; i < M; ++i) {
            cin >> holes[i+1][0] >> holes[i+1][1];
            C[i+1] = 0;
        }

        for (int i = 1; i < N+1; ++i) {
            G[i].clear();
            float x = gopers[i][0];
            float y = gopers[i][1];

            for (int j = 1; j < M+1; ++j) {
                float x_ = holes[j][0];
                float y_ = holes[j][1];

                if (sqrt(pow(x-x_, 2)+pow(y-y_, 2)) <= S*V) {
                    G[i].emplace_back(j);
                }
            }
        }

        for (int i = 1; i < N+1; ++i) {
            for (int j = 1; j < M+1; ++j) {
                U[j] = 0;
            }
            B(i);
        }
        
        int ans = 0;
        for (int i = 1; i < M+1; ++i) {
            if (C[i]) {
                ++ans;
            }
        }

        cout << N-ans << "\n";
    }


    return 0;
}