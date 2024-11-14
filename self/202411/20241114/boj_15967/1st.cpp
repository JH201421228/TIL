#include <iostream>
#include <vector>
using namespace std;

int N, Q1, Q2;
vector<long long> arr, tree, lazy;

long long I(int s, int e, int tree_idx) {
    if (s == e) {
        tree[tree_idx] = arr[s];
        return arr[s];
    }

    int mid = (s + e) >> 1;

    tree[tree_idx] = I(s, mid, tree_idx*2) + I(mid+1, e, tree_idx*2+1);
    
    return tree[tree_idx];
}

void lazy_U(int s, int e, int tree_idx) {
    if (lazy[tree_idx]) {
        tree[tree_idx] += (e-s+1) * lazy[tree_idx];
        if (s != e) {
            lazy[tree_idx*2] += lazy[tree_idx];
            lazy[tree_idx*2+1] += lazy[tree_idx];
        }
        lazy[tree_idx] = 0;
        return;
    }
    return;
}

void U(int s, int e, int l, int r, int tree_idx, int val) {
    lazy_U(s, e, tree_idx);

    if (s > r || e < l) {
        return;
    }

    if (s >= l && e <= r) {
        lazy[tree_idx] += (long long) val;
        lazy_U(s, e, tree_idx);
        return;
    }

    int mid = (s + e) >> 1;

    U(s, mid, l, r, tree_idx*2, val);
    U(mid+1, e, l, r, tree_idx*2+1, val);

    tree[tree_idx] = tree[tree_idx*2] + tree[tree_idx*2+1];
}

long long S(int s, int e, int l, int r, int tree_idx) {
    lazy_U(s, e, tree_idx);

    if (s > r || e < l) {
        return 0;
    }

    if (s >= l && e <= r) {
        return tree[tree_idx];
    }

    int mid = (s + e) >> 1;

    return S(s, mid, l, r, tree_idx*2) + S(mid+1, e, l, r, tree_idx*2+1);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> N >> Q1 >> Q2;

    arr.resize(N+1);
    tree.resize(4*N+1);
    lazy.resize(4*N+1);

    for (int i = 1; i < N+1; ++i) {
        cin >> arr[i];
    }

    I(1, N, 1);

    for (int i = 0; i < Q1 + Q2; ++i) {
        int q;
        cin >> q;

        if (q == 1) {
            int n, m;
            cin >> n >> m;
            cout << S(1, N, n, m, 1) << '\n';
        }
        else {
            int s, e, l;
            cin >> s >> e >> l;
            U(1, N, s, e, 1, l);
        }
    }

    return 0;
}