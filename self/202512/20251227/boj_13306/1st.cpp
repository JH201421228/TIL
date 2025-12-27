#include <iostream>
#include <stack>
#include <vector>
using namespace std;


int N, Q;
int tree[200'001];
int parent[200'001];
vector<string> ans;
stack<pair<int, int>> question;


int find(int idx) {
    int root = idx;

    while (root != tree[root]) root = tree[root];

    while (idx != root) {
        int parent = tree[idx];
        tree[idx] = root;
        idx = parent;
    }

    return root;
}


void union_parent(int idx) {
    int p = find(parent[idx]);

    tree[idx] = p;

    return;
}


void solve() {
    cin >> N >> Q;

    parent[1] = 1;
    for (int idx = 0; idx < N-1; ++idx) cin >> parent[idx+2];
    for (int idx = 0; idx < N+1; ++idx) tree[idx] = idx;

    for (int i = 0; i < N+Q-1; ++i) {
        int flag; cin >> flag;
        if (flag) {
            int a, b; cin >> a >> b;
            question.push({a, b});
        }
        else {
            int a; cin >> a;
            question.push({0, a});
        }
    }

    while (!question.empty()) {
        auto cur_question = question.top(); question.pop();

        if (cur_question.first) {
            if (find(cur_question.first) == find(cur_question.second)) ans.emplace_back("YES");
            else ans.emplace_back("NO");
        }
        else union_parent(cur_question.second);
    }

    for (int idx = ans.size(); idx > 0; --idx) cout << ans[idx-1] << '\n';

    return;
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    
    solve();

    return 0;
}