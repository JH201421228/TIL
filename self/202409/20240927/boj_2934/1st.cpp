#include <iostream>
#include <vector>
using namespace std;

vector<int> tree(100000*4+1);
vector<int> lazy(100000*4+1);
int MAX = 100000;

void lazy_U(int s, int e, int tree_idx) {
    if (lazy[tree_idx]) {
        tree[tree_idx] += (e-s+1) * lazy[tree_idx];
        if (s != e) {
            lazy[tree_idx*2] += lazy[tree_idx];
            lazy[tree_idx*2+1] += lazy[tree_idx];
        }
        lazy[tree_idx] = 0;
    }
}

int S(int s, int e, int tree_idx, int idx) {
    lazy_U(s, e, tree_idx);

    if (s > idx || e < idx) {
        return 0;
    }

    if (s == e) {
        return tree[tree_idx];
    }

    int mid = (s + e) / 2;

    return S(s, mid, tree_idx*2, idx) + S(mid+1, e, tree_idx*2+1, idx);
}

void U(int s, int e, int tree_idx, int l, int r, int v) {
    lazy_U(s, e, tree_idx);

    if (s > r || e < l) {
        return;
    }

    if (s >= l && e <= r) {
        lazy[tree_idx] += v;
        lazy_U(s, e, tree_idx);
        return;
    }

    int mid = (s + e) / 2;

    U(s, mid, tree_idx*2, l, r, v);
    U(mid+1, e, tree_idx*2+1, l, r, v);

    tree[tree_idx] = tree[tree_idx*2] + tree[tree_idx*2+1];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int N; cin >> N;

    for (int i = 0; i < N; ++i) {
        int a, b; cin >> a >> b;

        cout << S(1, MAX, 1, a) + S(1, MAX, 1, b) << "\n";

        U(1, MAX, 1, a, b, 1);
        U(1, MAX, 1, a, a, -S(1, MAX, 1, a));
        U(1, MAX, 1, b, b, -S(1, MAX, 1, b));
    }

    return 0;
}