#include <iostream>
#include <vector>
#include <queue>
#include <unordered_map>
using namespace std;

int N, P;
vector<int> G[801];
unordered_map<int, int> C;
int L[801];

void set_edge(int u, int v) {
    G[u].emplace_back(v);
    G[v].emplace_back(u);
    C[u*801+v] = 1;
    C[v*801+u] = 0;
}

bool bfs(int src, int sink) {
    fill(L, L+801, -1);
    L[src] = 0;
    queue<int> q;
    q.push(src);

    while (q.size() > 0) {
        int u = q.front(); q.pop();

        for (auto& v : G[u]) {
            if (L[v] == -1 && C[u*801+v] > 0) {
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
        if (L[v] == L[u]+1 && C[u*801+v] > 0) {
            int flow = dfs(v, sink);
            if (flow > 0) {
                C[u*801+v] -= flow;
                C[v*801+u] += flow;
                return flow;
            }
        }
    }

    return 0;
}

int max_flow(int src, int sink) {
    int ans = 0;

    while (bfs(src, sink)) {
        while (true) {
            int flow = dfs(src, sink);
            if (flow == 0) {
                break;
            }
            else {
                ans += flow;
            }
        }
    }

    return ans;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> N >> P;

    for (int i = 3; i < N+1; ++i) {
        set_edge(i, i+N);
    }

    for (int i = 0; i < P; ++i) {
        int u, v; cin >> u >> v;

        if (u > 2) {
            set_edge(u+N, v);
        }
        else {
            set_edge(u, v);
        }

        if (v > 2) {
            set_edge(v+N, u);
        }
        else {
            set_edge(v, u);
        }
    }

    cout << max_flow(1, 2) << '\n';

    return 0;
}