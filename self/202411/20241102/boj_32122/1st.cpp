#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int N;
vector<vector<int>> G;
vector<vector<int>> adj;
vector<int> C, U, W;

vector<pair<int, pair<int, int>>> E;
int delta[4][2] = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};

// DFS를 통해 매칭을 시도하는 함수
bool B(int n, vector<int> &V) {
    for (int x : adj[n]) {
        if (V[x]) continue;
        V[x] = 1;

        if (!C[x] || B(C[x], V)) {
            C[x] = n;
            return true;
        }
    }
    return false;
}

int main() {
    // 입력 처리
    cin >> N;
    G.resize(N, vector<int>(N));
    adj.resize(N * N / 2 + 1);

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            cin >> G[i][j];
        }
    }

    // 인접 리스트 구성 및 우선순위 큐에 엣지 추가
    priority_queue<pair<int, pair<int, int>>, vector<pair<int, pair<int, int>>>, greater<>> pq;
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            if ((i + j) % 2 == 0) {
                for (auto [di, dj] : delta) {
                    int ni = i + di, nj = j + dj;
                    if (ni >= 0 && ni < N && nj >= 0 && nj < N) {
                        pq.push({max(G[i][j], G[ni][nj]), {(i * N + j) / 2 + 1, (ni * N + nj) / 2 + 1}});
                    }
                }
            }
        }
    }

    C.assign(N * N / 2 + 1, 0);
    U.assign(N * N / 2 + 1, 0);
    W.assign(N * N / 2 + 1, 0);

    int val = 1, check = 0;
    vector<int> ans;

    // 매칭 및 값 추적
    while (!pq.empty()) {
        auto [v, ab] = pq.top(); pq.pop();
        int a = ab.first, b = ab.second;
        adj[a].push_back(b);
        W[a] = 1;

        for (int i = 1; i <= N * N / 2; ++i) {
            if (!U[i] && W[i]) {
                vector<int> V(N * N / 2 + 1, 0);
                if (B(i, V)) {
                    U[i] = 1;
                    ++check;
                }
            }
        }

        if (check == val) {
            ++val;
            ans.push_back(v);
        }
    }

    // 결과 출력
    for (int a : ans) {
        cout << a << "\n";
    }

    return 0;
}
