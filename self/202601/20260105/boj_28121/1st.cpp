#include <iostream>
#include <unordered_set>
using namespace std;


int N, Q;
int parent[300'001];
int odd[300'001];
int is_ans[300'001];
unordered_set<int> sets[300'001];
int ans;
string output;


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


int union_find(int a, int b) {
    int pa = find(a);
    int pb = find(b);

    if (is_ans[pa] || is_ans[pb]) {
        if (!is_ans[pa]) {
            ans += sets[pa].size();
            is_ans[pa] = 1;
        }
        if (!is_ans[pb]) {
            ans += sets[pb].size();
            is_ans[pb] = 1;
        }
    }

    if (sets[pa].size() < sets[pb].size()) swap(sets[pa], sets[pb]);

    parent[pb] = pa;

    if (odd[a] == odd[b]) {
        for (auto& v : sets[pb]) {
            sets[pa].insert(v);
            odd[v] = 1 - odd[v];
        }
        sets[pb].clear();
    }
    else {
        sets[pa].insert(sets[pb].begin(), sets[pb].end());
        sets[pb].clear();
    }

    return ans;
}


void solve() {
    cin >> N >> Q;

    for (int idx = 0; idx < N+1; ++idx) {
        parent[idx] = idx;
        sets[idx].insert(idx);
    }

    ans = 0;

    output = "";

    for (int i = 0; i < Q; ++i) {
        int a, b; cin >> a >> b;
        int pa = find(a);
        int pb = find(b);

        if (pa == pb && odd[a] == odd[b] && !is_ans[pa])  {
            is_ans[pa] = 1;
            ans += sets[pa].size();
        }

        if (pa != pb) ans = union_find(a, b);

        output += to_string(ans) + "\n";
    }

    cout << output << '\n';

    return;
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    solve();

    return 0;
}