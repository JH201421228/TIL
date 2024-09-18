#include <iostream>
#include <vector>
using namespace std;


vector<long long> arr;
vector<long long> arr_;
vector<long long> lazy;
vector<long long> tree;

long long I (int s, int e, int tree_idx) {
    if (s == e) {
        tree[tree_idx] = arr_[s];
        return arr_[s];
    }

    int mid = (s + e) / 2;

    tree[tree_idx] = I(s, mid, tree_idx*2) + I(mid+1, e, tree_idx*2+1);
    
    return tree[tree_idx];
}

void lazy_U (int s, int e, int tree_idx) {
    if (lazy[tree_idx]) {
        tree[tree_idx] += (e-s+1) * lazy[tree_idx];
        if (s != e) {
            lazy[tree_idx*2] += lazy[tree_idx];
            lazy[tree_idx*2+1] += lazy[tree_idx];
        }
        lazy[tree_idx] = 0;
    }
}

long long S (int s, int e, int tree_idx, int l, int r) {
    lazy_U(s, e, tree_idx);

    if (s > r || e < l) {
        return 0;
    }

    if (s >= l && e <= r) {
        return tree[tree_idx];
    }

    int mid = (s + e) / 2;

    return S(s, mid, tree_idx*2, l, r) + S(mid+1, e, tree_idx*2+1, l, r);
}

void U (int s, int e, int tree_idx, int l, int r, int v) {
    lazy_U(s, e, tree_idx);

    if (s > r || e < l) {
        return;
    }

    if (s >= l && e <= r) {
        tree[tree_idx] += (long long) (e-s+1) * v;
        if (s != e) {
            lazy[tree_idx*2] += (long long) v;
            lazy[tree_idx*2+1] += (long long) v;
        }
        return;
    }

    int mid = (s + e) / 2;

    U(s, mid, tree_idx*2, l, r, v);
    U(mid+1, e, tree_idx*2+1, l, r, v);

    tree[tree_idx] = tree[tree_idx*2] + tree[tree_idx*2+1];
}

int main () {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int N;
    cin >> N;

    arr.resize(N+1);
    arr_.resize(N+1);
    tree.resize(4*N+1);
    lazy.resize(4*N+1);

    for (int i = 0; i < N; ++i) {
        cin >> arr[i+1];
        arr_[i+1] = arr[i+1] - arr[i];
    }

    I(1, N, 1);

    int Q;
    cin >> Q;

    for (int i = 0; i < Q; ++i) {
        int a;
        cin >> a;

        if (a == 1) {
            int b, c;
            cin >> b >> c;
            U(1, N, 1, b, c, 1);
            if (c != N) {
                U(1, N, 1, c+1, c+1, -(c-b+1));
            }
        }
        else {
            int b;
            cin >> b;
            cout << S(1, N, 1, 1, b) << "\n";
        }
    }

    return 0;
}