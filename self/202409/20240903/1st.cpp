#include <iostream>
#include <vector>
using namespace std;

vector<int> arr;
vector<int> tree;
vector<int> fake;
vector<int> lazy;


int I (int s, int e, int tree_idx) {
    if (s == e) {
        fake[tree_idx] = 1;
        return 1;
    }

    int mid = (s + e) / 2;

    fake[tree_idx] = I(s, mid, tree_idx*2) + I(mid+1, e, tree_idx*2+1);
    return fake[tree_idx];
}

void lazy_U (int s, int e, int tree_idx) {
    if (lazy[tree_idx]) {
        tree[tree_idx] = fake[tree_idx] - tree[tree_idx];
        if (s != e) {
            lazy[tree_idx*2] = 1 - lazy[tree_idx*2];
            lazy[tree_idx*2+1] = 1 - lazy[tree_idx*2+1];
        }
        lazy[tree_idx] = 0;
    }
}

int S (int s, int e, int tree_idx, int l, int r) {
    lazy_U(s, e, tree_idx);

    if (l > e || r < s) {
        return 0;
    }

    if (s >= l && e <= r) {
        return tree[tree_idx];
    }

    int mid = (s + e) / 2;

    return S(s, mid, tree_idx*2, l, r) + S(mid+1, e, tree_idx*2+1, l, r);
}

void U (int s, int e, int tree_idx, int l, int r) {
    lazy_U(s, e, tree_idx);

    if (s > r || e < l) {
        return;
    }

    if (s >= l && e <= r) {
        tree[tree_idx] = fake[tree_idx] - tree[tree_idx];
        if (s != e) {
            lazy[tree_idx*2] = 1 - lazy[tree_idx*2];
            lazy[tree_idx*2+1] = 1 - lazy[tree_idx*2+1];
        }
        return;
    }

    int mid = (s + e) / 2;

    U(s, mid, tree_idx*2, l, r);
    U(mid+1, e, tree_idx*2+1, l, r);

    tree[tree_idx] = tree[tree_idx*2] + tree[tree_idx*2+1];
}


int main () {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int N, M;

    cin >> N >> M;

    arr.resize(N+1);
    lazy.resize(4*N+1);
    tree.resize(4*N+1);
    fake.resize(4*N+1);

    I(1, N, 1);

    for (int i = 0; i < M; ++i) {
        int o, s, t;
        cin >> o >> s >> t;

        if (o) {
            cout << S(1, N, 1, s, t) << '\n';
        }
        else {
            U(1, N, 1, s, t);
        }
    }

    return 0;
}