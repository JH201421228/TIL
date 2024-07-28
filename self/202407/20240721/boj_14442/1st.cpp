#include <iostream>
#include <vector>
#include <queue>
using namespace std;


struct State {
    int i, j, k;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int N, M, K;
    cin >> N >> M >> K;

    if (N == 1 and M == 1) {
        cout << 1;
        return 0;
    }

    vector<vector<int>> G(N, vector<int>(M));
    char n;
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            cin >> n;
            G[i][j] = n - '0';
        }
    }

    vector<vector<vector<int>>> V(N, vector<vector<int>>(M, vector<int>(K+1, 0)));
    V[0][0][0] = 1;

    int delta[4][2] = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
    
    queue<State> q;
    q.push({0, 0, 0});

    while (!q.empty()) {
        State s = q.front();
        q.pop();

        for (auto& d: delta) {
            int ii = s.i + d[0], jj = s.j + d[1];
            if (ii >= 0 && ii < N && jj >= 0 && jj < M) {
                if (!G[ii][jj] && !V[ii][jj][s.k]) {
                    V[ii][jj][s.k] = V[s.i][s.j][s.k] + 1;
                    q.push({ii, jj, s.k});
                    if (ii == N-1 && jj == M-1) {
                        cout << V[ii][jj][s.k];
                        return 0;
                    }
                }
                else if (G[ii][jj] && s.k < K && !V[ii][jj][s.k+1]) {
                    V[ii][jj][s.k+1] = V[s.i][s.j][s.k] + 1;
                    q.push({ii, jj, s.k+1});
                    if (ii == N-1 && jj == M-1) {
                        cout << V[ii][jj][s.k+1];
                        return 0;
                    }
                }
            }
        }
    }

    cout << -1;

    return 0;
}