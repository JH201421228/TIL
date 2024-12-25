#include <iostream>
#include <vector>
#include <queue>
#include <unordered_map>
using namespace std;

const int MAXN = 800; // 최대 노드 수 (2 * N 까지 고려)

vector<int> G[MAXN];
unordered_map<int, int> C;

void set_edge(int i, int j) {
    G[i].push_back(j);
    G[j].push_back(i);
    C[i * MAXN + j] = 1; // 용량 설정
    C[j * MAXN + i] = 0; // 역방향 간선 초기화
}

vector<int> bfs(int src, int sink, int n) {
    vector<int> L(2 * n + 1, -1);
    L[src] = 0;
    queue<int> q;
    q.push(src);

    while (!q.empty()) {
        int u = q.front();
        q.pop();

        for (int v : G[u]) {
            if (L[v] == -1 && C[u * MAXN + v] > 0) {
                L[v] = L[u] + 1;
                q.push(v);
            }
        }
    }

    return L;
}

int dfs(int u, int sink, vector<int>& L) {
    if (u == sink) return 1;

    for (int v : G[u]) {
        if (L[v] == L[u] + 1 && C[u * MAXN + v] > 0) {
            int k = dfs(v, sink, L);
            if (k > 0) {
                C[u * MAXN + v] -= k; // 유량 감소
                C[v * MAXN + u] += k; // 역방향 유량 증가
                return k;
            }
        }
    }

    return 0;
}

int max_flow(int src, int sink, int n) {
    int total = 0;

    while (true) {
        vector<int> L = bfs(src, sink, n);
        if (L[sink] == -1) return total;

        while (true) {
            int flow = dfs(src, sink, L);
            if (flow == 0) break;
            total += flow;
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N, P;
    cin >> N >> P;

    for (int i = 3; i <= N; ++i) {
        set_edge(i, i + N);
    }

    for (int i = 0; i < P; ++i) {
        int u, v;
        cin >> u >> v;

        if (u > 2) {
            set_edge(u + N, v);
        } else {
            set_edge(u, v);
        }

        if (v > 2) {
            set_edge(v + N, u);
        } else {
            set_edge(v, u);
        }
    }

    cout << max_flow(1, 2, N) << "\n";

    return 0;
}
