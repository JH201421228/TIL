#include <iostream>
#include <unordered_map>
#include <vector>
#include <stack>
using namespace std;

int K, N, O = 0, cnt = 0;
int V[10002], F[10002];
stack<int> S;
vector<int> G[10002];

unordered_map<char, int> color{
    {'R', 0},
    {'B', 1}
};

void minor_setting(int a, int b, int c, int d) {
    G[b].emplace_back(a);
    G[c].emplace_back(d);

    return;
}

void setting(int a, char b, int c, char d, int e, char f) {
    minor_setting(2*a+color[b], 2*c+1-color[d], 2*a+1-color[b], 2*c+color[d]);
    minor_setting(2*a+color[b], 2*e+1-color[f], 2*a+1-color[b], 2*e+color[f]);
    minor_setting(2*c+color[d], 2*e+1-color[f], 2*c+1-color[d], 2*e+color[f]);

    return;
}

int scc(int n) {
    int p = ++O;
    V[n] = O;
    S.push(n);

    for (int x : G[n]) {
        if (!V[x]) p = min(p, scc(x));
        else if (!F[x]) p = min(p, V[x]);
    }

    if (p == V[n]) {
        ++cnt;

        while (!S.empty()) {
            int o = S.top(); S.pop();
            F[o] = cnt;

            if (o == n) break;
        }
    }

    return p;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> K >> N;

    for (int i = 0; i < N; ++i) {
        int a, c, e;
        char b, d, f;
        cin >> a >> b >> c >> d >> e >> f;
        setting(a, b, c, d, e, f);
    }

    for (int n = 2; n < 2*K+2; ++n) {
        if (!V[n]) scc(n);
    }

    string ans = "";

    for (int n = 1; n < K+1; ++n) {
        if (F[2*n] == F[2*n+1]) {
            cout << -1 << '\n';
            return 0;
        }
        else if (F[2*n] < F[2*n+1]) ans += 'R';
        else ans += 'B';
    }

    cout << ans << '\n';

    return 0;
}