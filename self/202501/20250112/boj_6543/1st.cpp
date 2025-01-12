#include <iostream>
#include <stack>
#include <vector>
#include <algorithm>
using namespace std;

int V[5001];
int F[5001];
int O = 0;
int cnt = 0;

int Vt[5001], Vc[5001];
vector<int> ans_list;

int N, M;

vector<int> G[5001];

stack<int> S;

int scc(int n) {
    int p = ++O;
    V[n] = O;
    S.push(n);

    for (auto& x : G[n]) {
        if (!V[x]) {
            p = min(scc(x), p);
        }
        else if (!F[x]) {
            p = min(V[x], p);
        }
    }

    if (p == V[n]) {
        ++cnt;
        while (!S.empty()) {
            int o = S.top(); S.pop();
            F[o] = cnt;

            if (o == n) {
                break;
            }
        }
    }

    return p;
}

bool dfs(int n, int flag) {
    Vt[n] = 1;

    for (auto& x : G[n]) {
        if (!Vt[x]) {
            if (F[x] != flag) {
                return false;
            }

            if (!dfs(x, flag)) {
                return false;
            }
        }
    }

    return true;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    while (true) {
        fill(V, V+5001, 0);
        fill(F, F+5001, 0);
        for (int i = 0; i < 5001; ++i) G[i].clear();

        cin >> N; if (!N) break; cin >> M;

        for (int i = 0; i < M; ++i) {
            int u, v; cin >> u >> v;

            G[u].emplace_back(v);
        }

        cnt = O = 0;
        for (int i = 1; i < N+1; ++i) {
            if (!V[i]) {
                scc(i);
            }
        }

        fill(Vc, Vc+5001, 0);
        ans_list.clear();

        for (int i = 1; i < N+1; ++i) {
            if (!Vc[F[i]]) {
                Vc[F[i]] = 1;
                fill(Vt, Vt+5001, 0);
                if (dfs(i, F[i])) {
                    ans_list.emplace_back(F[i]);
                }
            }
        }

        for (int i = 0; i < N+1; ++i) {
            if (find(ans_list.begin(), ans_list.end(), F[i]) != ans_list.end()) {
                cout << i << " ";
            }
        }
        cout << '\n';
    }

    return 0;
}