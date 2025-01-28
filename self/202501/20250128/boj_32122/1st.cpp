#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <cstring>

using namespace std;

const int MAXN = 10000; // N^2 최대 크기

vector<int> G[MAXN + 1];
vector<pair<int, int>> temp[MAXN + 1];
int C[MAXN + 1];
bool U[MAXN + 1];
bool V[MAXN + 1];

int N;
int M[100][100];

bool B(int n) {
    for (int x : G[n]) {
        if (V[x]) continue;
        V[x] = true;

        if (!C[x] || B(C[x])) {
            C[x] = n;
            C[n] = x;
            return true;
        }
    }
    return false;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> N;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> M[i][j];
        }
    }

    int delta[4][2] = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};

    for (int i = 0; i < N * N; i++) {
        int x = i / N;
        int y = i % N;

        if ((x % 2 + y % 2) != 1) {
            for (int d = 0; d < 4; d++) {
                int xx = x + delta[d][0];
                int yy = y + delta[d][1];
                
                if (xx >= 0 && xx < N && yy >= 0 && yy < N) {
                    temp[max(M[x][y], M[xx][yy])].emplace_back(x * N + y + 1, xx * N + yy + 1);
                }
            }
        }
    }

    memset(U, 0, sizeof(U));
    memset(C, 0, sizeof(C));

    vector<int> ans;

    for (int i = 1; i <= N * N; i++) {
        if (!temp[i].empty()) {
            for (auto& p : temp[i]) {
                int u = p.first;
                int v = p.second;
                G[u].push_back(v);
                G[v].push_back(u);
            }

            for (auto& p : temp[i]) {
                int u = p.first;
                int v = p.second;

                if (!U[u] && !U[v]) {
                    U[u] = true;
                    U[v] = true;
                    C[u] = v;
                    C[v] = u;
                    ans.push_back(i);
                } else if (!U[u]) {
                    U[u] = true;
                    memset(V, 0, sizeof(V));
                    if (B(u)) {
                        ans.push_back(i);
                    }
                } else if (!U[v]) {
                    U[v] = true;
                    memset(V, 0, sizeof(V));
                    if (B(v)) {
                        ans.push_back(i);
                    }
                }
            }
        }
    }

    for (int n : ans) {
        cout << n << "\n";
    }

    return 0;
}
