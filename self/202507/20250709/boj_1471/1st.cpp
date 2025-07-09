#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>
using namespace std;

int N, O = 0, C = 0;
int G[200001], F[200001], V[200001];
stack<int> S;
vector<vector<int>> L;

int get_next(int n) {
    int res = n;
    while (n > 0) {
        res += n%10;
        n /= 10;
    }

    return res;
}

int scc(int n) {
    int p = ++O;
    V[n] = p;
    S.push(n);

    int x = G[n];
    if (!V[x]) p = min(p, scc(x));
    else if (!F[x]) p = min(p, V[x]);

    if (p == V[n]) {
        vector<int> temp;

        while (!S.empty()) {
            int o = S.top(); S.pop();
            temp.emplace_back(o);
            F[o] = 1;

            if (o == n) {
                L.emplace_back(temp);
                break;
            }
        }
    }

    return p;
}

int get_max_value(int n) {
    int x = G[n];

    if (x == n) F[n] = 1;
    else if (F[x] != 1) F[n] = F[x] + 1;
    else F[n] = get_max_value(x) + 1;

    return F[n];
}

int solve() {
    cin >> N;

    for (int n = 1; n < N+1; ++n) {
        int x = get_next(n);
        if (x < N+1) G[n] = x;
        else if (x % N == 0) G[n] = N;
        else G[n] = x % N;
    }

    for (int n = 1; n < N+1; ++n) {
        if (!V[n]) scc(n);
    }

    for (vector<int> temp : L) {
        int val = temp.size();

        for (int v : temp) F[v] = val;
    }

    for (int n = 1; n < N+1; ++n) {
        if (F[n] == 1) get_max_value(n);
    }

    return *max_element(F, F + 200001);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cout << solve() << '\n';

    return 0;
}