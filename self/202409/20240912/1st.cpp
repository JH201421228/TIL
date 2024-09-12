#include <iostream>
#include <vector>
using namespace std;


vector<int> arr;
vector<int> tree;
vector<int> lazy;

int I (int s, int e, int tree_idx) {
    if (s == e) {
        tree[tree_idx] = arr[s];
        return arr[s];
    }

    int mid = (s + e) / 2;
    
    tree[tree_idx] = I(s, mid, tree_idx*2) ^ I(mid+1, e, tree_idx*2+1);
    
    return tree[tree_idx];
}

void lazy_U (int s, int e, int tree_idx) {
    if (lazy[tree_idx]) {
        if ((e-s+1) % 2) {
            tree[tree_idx] ^= lazy[tree_idx];
        }
        if (s != e) {
            lazy[tree_idx*2] ^= lazy[tree_idx];
            lazy[tree_idx*2+1] ^= lazy[tree_idx];
        }
        lazy[tree_idx] = 0;
    }
}

int S (int s, int e, int tree_idx, int l, int r) {
    lazy_U(s, e, tree_idx);

    if (s > r || e < l) {
        return 0;
    }

    if (s >= l && e <= r) {
        return tree[tree_idx];
    }

    int mid = (s + e) / 2;

    return S(s, mid, tree_idx*2, l, r) ^ S(mid+1, e, tree_idx*2+1, l, r);
}

void U (int s, int e, int tree_idx, int l, int r, int val) {
    lazy_U(s, e, tree_idx);

    if (s > r || e < l) {
        return;
    }

    if (s >= l && e <= r) {
        if ((e-s+1) % 2) {
            tree[tree_idx] ^= val;
        }
        if (s != e) {
            lazy[tree_idx*2] ^= val;
            lazy[tree_idx*2+1] ^= val;
        }
        return;
    }

    int mid = (s + e) / 2;

    U(s, mid, tree_idx*2, l, r, val);
    U(mid+1, e, tree_idx*2+1, l, r, val);
    
    tree[tree_idx] = tree[tree_idx*2] ^ tree[tree_idx*2+1];
}

int main () {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int N, M;
    cin >> N;

    arr.resize(N+1);
    tree.resize(4*N+1);
    lazy.resize(4*N+1);

    for (int i = 0; i < N; ++i) {
        cin >> arr[i+1];
    }

    I(1, N, 1);

    cin >> M;

    for (int i = 0; i < M; ++i) {
        int a;
        cin >> a;

        if (a == 1) {
            int b, c, d;
            cin >> b >> c >> d;

            U(1, N, 1, b+1, c+1, d);
        }
        else {
            int b, c;
            cin >> b >> c;

            cout << S(1, N, 1, b+1, c+1) << "\n";
        }
    }

    return 0;
}