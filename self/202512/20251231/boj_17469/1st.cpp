#include <iostream>
#include <unordered_set>
#include <stack>
#include <vector>
using namespace std;


int N, Q;
int parent[100'001], tree[100'001];
unordered_set<int> sets[100'001];
stack<pair<int, int>> questions;
vector<int> ans;


int find(int idx) {
    int root = idx;

    while (root != tree[root]) root = tree[root];

    while (root != idx) {
        int cur = idx;
        idx = tree[idx];
        tree[cur] = root;
    }

    return root;
}


void union_tree(int idx) {
    int p = find(parent[idx]);
    tree[idx] = p;

    if (sets[p].size() < sets[idx].size()) swap(sets[p], sets[idx]);

    sets[p].insert(sets[idx].begin(), sets[idx].end());
    sets[idx].clear();

    return;
}


void solve() {
    cin >> N >> Q;

    parent[1] = 1;
    for (int idx = 0; idx < N-1; ++idx) cin >> parent[idx+2];

    for (int idx = 0; idx < N; ++idx) {
        int tmp; cin >> tmp;
        sets[idx+1].insert(tmp);
    }

    for (int i = 0; i < N+Q-1; ++i) {
        int a, b; cin >> a >> b;
        questions.push({a, b});
    }

    for (int idx = 0; idx < N+1; ++idx) tree[idx] = idx;

    while (!questions.empty()) {
        pair<int, int> cur_question = questions.top(); questions.pop();

        if (cur_question.first == 1) union_tree(cur_question.second);
        else ans.emplace_back(sets[find(cur_question.second)].size());
    }

    for (int idx = Q; idx > 0; --idx) {
        cout << ans[idx-1] << '\n';
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