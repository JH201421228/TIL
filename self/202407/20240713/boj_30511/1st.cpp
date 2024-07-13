#include <vector>
#include <iostream>
#include <string>
using namespace std;

const int MAX = 101;
vector<int> G[10001];
int C[10001];
int V[10001];
int Ss[MAX][MAX], Sg[MAX][MAX];

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

int main () {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N, M;
    cin >> N >> M;

    vector<string> S(N);
    for (int i = 0; i < N; i++) {
        cin >> S[i];
    }
    
    int cnt_s = 0, cnt_g = 0;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            if (S[i][j] == 'S') {
                Ss[i][j] = ++cnt_s;
            }
            else if (S[i][j] == 'G') {
                Sg[i][j] = ++cnt_g;
            }
        }
    }

    vector<pair<int, int>> delta = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}, {1, 1}, {1, -1}, {-1, 1}, {-1, -1}};
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            if (S[i][j] == 'S') {
                for (auto d : delta) {
                    int ii = i+d.first, jj = j+d.second;
                    if (ii >= 0 && ii < N && jj >= 0 && jj < M) {
                        if (S[ii][jj] == 'G') {
                            if ((i + 2 * d.first >= 0 && i + 2 * d.first < N && j + 2 * d.second >= 0 && j + 2 * d.second < M && S[i + 2 * d.first][j + 2 * d.second] == 'M') || (i - d.first >= 0 && i - d.first < N && j - d.second >= 0 && j - d.second < M && S[i - d.first][j - d.second] == 'M')) {
                                G[Ss[i][j]].emplace_back(Sg[ii][jj]);
                            }
                        }
                    }
                }
            }
        }
    }

    int ans = 0;
    for (int i = 1; i <= cnt_s; i++) {
        fill(V, V+cnt_g+1, 0);
        if (B(i)) {
            ++ans;
        }
    }

    cout << ans << '\n';

    return 0;
}