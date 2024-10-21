#include <iostream>
#include <vector>
using namespace std;

int M[201][201];
int cur[201];
int V[401];
int F[401];
int s = 0;
int e = 0;
int O = 0;
int cnt = 0;
int mid = 0;
vector<int> S;
vector<int> G[401];

void connect(int t, int N) {
    for (int i = 1; i < N+1; ++i) {
        for (int j = t+1; j < N; ++j) {
            int a = i;
            int b = M[i][j];

            if (cur[a] == cur[b]) {
                G[a].emplace_back(401-b);
                G[401-a].emplace_back(b);
                G[b].emplace_back(401-a);
                G[401-b].emplace_back(a);
            }
            else if ((cur[a]+1) % 3 == (cur[b]+2) % 3) {
                G[a].emplace_back(b);
                G[401-b].emplace_back(401-a);
            }
            else {
                G[b].emplace_back(a);
                G[401-a].emplace_back(401-b);
            }
        }
    }
}

int scc(int n) {
    int p = V[n] = ++O;
    S.emplace_back(n);

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
            int out = S.back();
            S.pop_back();
            F[out] = cnt;

            if (out == n) {
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

    int N; cin >> N;

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            if (j == 0) {
                cin >> cur[i+1];
            }
            else {
                cin >> M[i+1][j];
            }
        }
    }
    
    e = N;

    while (s <= e) {
        bool checker = true;

        for (int i = 0; i < 401; ++i) {
            G[i].clear();
            V[i] = 0;
            F[i] = 0;
        }
        S.clear();
        O = 0;
        cnt = 0;

        mid = (s+e) / 2;

        connect(mid, N);
        
        for (int i = 1; i < N+1; ++i) {
            if (!V[i]) {
                scc(i);
            }
            if (!V[401-i]) {
                scc(401-i);
            }
        }

        for (int i = 1; i < N+1; ++i) {
            if (F[i] == F[401-i]) {
                s = mid + 1;
                checker = false;
                break;
            }
        }
        if (checker) {
            e = mid - 1;
        }

    }

    cout << s << '\n';

    return 0;
}