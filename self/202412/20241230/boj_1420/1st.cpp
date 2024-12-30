#include <iostream>
#include <vector>
#include <queue>
using namespace std;


int N, P, C[401][401], L[401];
vector<int> G[401];

void set_edge(int u, int v) {
    G[u].emplace_back(v);
    G[v].emplace_back(u);
    C[u][v] = 1;
    C[v][u] = 0;

    return;
}

bool bfs(int src, int sink) {
    fill(L, L+401, -1);
    L[src] = 0;
    queue<int> q;
    q.push(src);

    while (!q.empty()) {
        int u = q.front(); q.pop();

        for (auto& v : G[u]) {
            if (L[v] == -1 && C[u][v] > 0) {
                L[v] = L[u]+1;
                q.push(v);
            }
        }
    }

    return L[sink] != -1;
}

int dfs(int u, int sink) {
    if (u == sink) {
        return 1;
    }

    for (auto& v : G[u]) {
        if (L[v] == L[u]+1 && C[u][v] > 0) {
            int k = dfs(v, sink);
            if (k > 0) {
                C[u][v] = 0;
                C[v][u] = 1;
                return 1;
            }
        }
    }

    return 0;
}

int get_ans(int src, int sink) {
    int ans = 0;

    while (bfs(src, sink)) {
        while (true) {
            int flow = dfs(src, sink);
            if (flow == 0) {
                break;
            }
            ans += flow;
        }
    }

    return ans;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> N >> P;

    for (int i = 0; i < P; ++i) {
        int u, v; cin >> u >> v;
        set_edge(u, v);
    }

    cout << get_ans(1, 2) << '\n';

    return 0;
}