#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

vector<long long> tree;

int S(int s, int e, long long v, int tree_idx) {
    if (s == e) {
        return s;
    }

    int mid = (s+e) / 2;
    if (tree[tree_idx*2] >= v) {
        return S(s, mid, v, tree_idx*2);
    }
    else {
        return S(mid+1, e, v-tree[tree_idx*2], tree_idx*2+1);
    }
}

void U(int s, int e, long long c, int idx, int tree_idx) {
    if (idx > e || idx < s) {
        return;
    }

    tree[tree_idx] += c;

    if (s == e) {
        return;
    }

    int mid = (s+e) / 2;
    U(s, mid, c, idx, tree_idx*2);
    U(mid+1, e, c, idx, tree_idx*2+1);
}

int main () {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int N;
    cin >> N;

    tree.resize(4000004);

    for (int i = 0; i < N; ++i) {
        int a;
        cin >> a;
        if (a == 1) {
            int b;
            cin >> b;
            int ans = S(1, 1000001, b, 1);
            cout << ans << '\n';
            U(1, 1000001, -1, ans, 1);
        }
        else {
            int b;
            long long c;
            cin >> b >> c;
            U(1, 1000001, c, b, 1);
        }
    }

    return 0;
}