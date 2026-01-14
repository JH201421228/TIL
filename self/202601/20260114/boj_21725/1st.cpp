#include <iostream>
#include <unordered_set>
using namespace std;


int N, M;
int parent[100'001];
long long state[100'001], debt[100'001];
unordered_set<int> sets[100'001];


int find(int idx) {
    int root = idx;

    while (root != parent[root]) root = parent[root];

    while (root != idx) {
        int p = parent[idx];
        parent[idx] = root;
        idx = p;
    }

    return root;
}


void union_find(int a, int b) {
    int pa = find(a);
    int pb = find(b);

    if (sets[pa].size() < sets[pb].size()) swap(pa, pb);

    parent[pb] = pa;

    long long cost = (debt[pa] / sets[pa].size()) - (debt[pb] / sets[pb].size());
    debt[pa] = (debt[pa] / sets[pa].size()) * (sets[pa].size() + sets[pb].size());

    for (auto& v : sets[pb]) {
        sets[pa].insert(v);
        state[v] += cost;
    }

    sets[pb].clear();

    return;
}


void solve() {
    cin >> N >> M;

    for (int i = 0; i < N+1; ++i) {
        parent[i] = i;
        sets[i].insert(i);
    }

    for (int i = 0; i < M; ++i) {
        int a, b; long long c; cin >> a >> b >> c;

        if (a == 1) union_find(b, c);
        else {
            debt[find(b)] += c;
            state[b] += c;
        }
    }

    int p = find(1);

    if (debt[p]) {
        long long cost = debt[p] / N;

        for (int idx = 1; idx < N+1; ++idx) state[idx] -= cost;
    }

    string ans = "";
    int cnt = 0;

    for (int idx = 1; idx < N+1; ++idx) {
        if (idx == p || !state[idx]) continue;

        ++cnt;

        if (state[idx] > 0) ans += to_string(p) + " " + to_string(idx) + " " + to_string(state[idx]) + "\n";
        else ans += to_string(idx) + " " + to_string(p) + " " + to_string(-state[idx]) + "\n";
    }

    cout << cnt << "\n" << ans;

    return;
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    solve();

    return 0;
}