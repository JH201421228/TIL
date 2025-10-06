#include <iostream>
#include <vector>
using namespace std;


const long long MAX = 300'000;

int N;
int V[MAX+1], nodes[MAX+1];
long long inner[MAX+1], outer[MAX+1];
vector<pair<int, int>> G[MAX+1];


void set_inner(int n) {
    nodes[n] = 1;

    for (auto& xd : G[n]) {
        if (!nodes[xd.first]) {
            set_inner(xd.first);
            nodes[n] += nodes[xd.first];
            inner[n] += inner[xd.first] + nodes[xd.first] * xd.second;
        }
    }

    return;
}


void set_outer(int n) {
    V[n] = 1;

    for (auto& xd : G[n]) {
        int x = xd.first, d = xd.second;
        if (!V[x]) {
            outer[x] = outer[n] + (N - nodes[n]) * d + inner[n] - (inner[x] + nodes[x] * d) + (nodes[n] - nodes[x]) * d;
            set_outer(x);
        }
    }

    return;
}


void solve() {
    cin >> N;
    for (int i = 0; i < N-1; ++i) {
        int u, v, d; cin >> u >> v >> d;
        G[u].emplace_back(v, d);
        G[v].emplace_back(u, d);
    }

    set_inner(1);
    set_outer(1);

    for (int i = 1; i < N+1; ++i) {
        cout << inner[i] + outer[i] << '\n';
    }

    return;
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    solve();

    return 0;
}