#include <iostream>
#include <vector>
#include <algorithm>
#include <stack>
using namespace std;

int N, M, interest[3001][5], prefer[3001][2], V[6001], F[6001], O = 0, cnt = 0;
vector<int> G[6001];
vector<pair<int, int>> leafs[500001], ans_list;
stack<int> S;

int scc(int n) {
    int p = ++O;
    V[n] = O;
    S.push(n);

    for (auto& x : G[n]) {
        if (!V[x]) {
            p = min(p, scc(x));
        }
        else if (!F[x]) {
            p = min(p, V[x]);
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

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> N >> M;

    for (int i = 1; i < N+1; ++i) {
        for (int j = 1; j < 5; ++j) {
            cin >> interest[i][j];
        }
    }

    for (int i = 1; i < N+1; ++i) {
        for (int j = 0; j < 2; ++j) {
            int t; cin >> t;
            prefer[i][j] = t;
            leafs[t].emplace_back(i, j);
        }
    }
    
    for (auto& leaf : leafs) {
        int n = leaf.size();
        for (int i = 0; i < n; ++i) {
            for (int j = i+1; j < n; ++j) {
                int an = leaf[i].first + leaf[i].second*N;
                int bn = leaf[j].first + leaf[j].second*N;
                if (an <= N && bn <= N) {
                    G[an].emplace_back(bn+N);
                    G[bn].emplace_back(an+N);
                }
                else if (an <= N && bn > N) {
                    G[an].emplace_back(bn-N);
                    G[bn].emplace_back(an+N);
                }
                else if (an > N && bn <= N) {
                    G[an].emplace_back(bn+N);
                    G[bn].emplace_back(an-N);
                }
                else {
                    G[an].emplace_back(bn-N);
                    G[bn].emplace_back(an-N);
                }
            }
        }
    }

    for (int i = 0; i < M; ++i) {
        int a, b, c; cin >> a >> b >> c;
        for (auto& a_leaf : leafs[a]) {
            for (auto& b_leaf : leafs[b]) {
                if (interest[a_leaf.first][c] != interest[b_leaf.first][c]) {
                    int an = a_leaf.first + a_leaf.second*N;
                    int bn = b_leaf.first + b_leaf.second*N;
                    if (an <= N && bn <= N) {
                        G[an].emplace_back(bn+N);
                        G[bn].emplace_back(an+N);
                    }
                    else if (an <= N && bn > N) {
                        G[an].emplace_back(bn-N);
                        G[bn].emplace_back(an+N);
                    }
                    else if (an > N && bn <= N) {
                        G[an].emplace_back(bn+N);
                        G[bn].emplace_back(an-N);
                    }
                    else {
                        G[an].emplace_back(bn-N);
                        G[bn].emplace_back(an-N);
                    }
                }
            }
        }
    }

    for (int i = 1; i < 2*N+1; ++i) {
        if (!V[i]) {
            scc(i);
        }
    }

    for (int i = 1; i < N+1; ++i) {
        if (F[i] == F[i+N]) {
            cout << "NO" << '\n';
            exit(0);
        }
        else if (F[i] > F[i+N]) {
            ans_list.emplace_back(prefer[i][1], i);
        }
        else {
            ans_list.emplace_back(prefer[i][0], i);
        }
    }

    cout << "YES" << '\n';

    sort(ans_list.begin(), ans_list.end());

    for (auto& ans : ans_list) {
        cout << ans.second << ' ';
    }

    return 0;
}