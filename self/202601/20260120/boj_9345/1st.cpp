#include <iostream>
#include <algorithm>
#include <climits>
using namespace std;


int T, N, K, Q, A, B;
int arr[100'001];
int max_tree[400'005], min_tree[400'005];


int I(int s, int e, int tree_idx, int flag, int* tree) {
    if (s == e) {
        tree[tree_idx] = arr[s];
        return arr[s];
    }

    int mid = (s+e)>>1;

    if (flag) tree[tree_idx] = max(I(s, mid, tree_idx<<1, flag, tree), I(mid+1, e, tree_idx<<1|1, flag, tree));
    else tree[tree_idx] = min(I(s, mid, tree_idx<<1, flag, tree), I(mid+1, e, tree_idx<<1|1, flag, tree));

    return tree[tree_idx];
}


void U(int s, int e, int idx, int tree_idx, int flag, int* tree) {
    if (idx > e || idx < s) return;

    if (s == e) {
        tree[tree_idx] = arr[idx];
        return;
    }

    int mid = (s+e)>>1;

    U(s, mid, idx, tree_idx<<1, flag, tree);
    U(mid+1, e, idx, tree_idx<<1|1, flag, tree);

    if (flag) tree[tree_idx] = max(tree[tree_idx<<1], tree[tree_idx<<1|1]);
    else tree[tree_idx] = min(tree[tree_idx<<1], tree[tree_idx<<1|1]);

    return;
}


int S(int s, int e, int l, int r, int tree_idx, int flag, int* tree) {
    if (s >= l && e <= r) return tree[tree_idx];

    if (s > r || e < l) {
        if (flag) return 0;
        else return INT_MAX;
    }

    int mid = (s+e)>>1;

    if (flag) return max(S(s, mid, l, r, tree_idx<<1, flag, tree), S(mid+1, e, l, r, tree_idx<<1|1, flag, tree));
    else return min(S(s, mid, l, r, tree_idx<<1, flag, tree), S(mid+1, e, l, r, tree_idx<<1|1, flag, tree));
}


void solve() {
    cin >> N >> K;

    for (int idx = 0; idx < N; ++idx) arr[idx] = idx;
    for (int idx = 0; idx < 4*N+1; ++idx) {
        max_tree[idx] = 0;
        min_tree[idx] = INT_MAX;
    }

    I(0, N-1, 1, 1, max_tree);
    I(0, N-1, 1, 0, min_tree);

    for (int i = 0; i < K; ++i) {
        cin >> Q >> A >> B;

        if (Q) {
            if (A == S(0, N-1, A, B, 1, 0, min_tree) && B == S(0, N-1, A, B, 1, 1, max_tree)) cout << "YES" << '\n';
            else cout << "NO" << '\n';
        }
        else {
            swap(arr[A], arr[B]);

            U(0, N-1, A, 1, 0, min_tree);
            U(0, N-1, B, 1, 0, min_tree);
            U(0, N-1, A, 1, 1, max_tree);
            U(0, N-1, B, 1, 1, max_tree);
        }
    }

    return;
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> T;

    while (T--) solve();

    return 0;
}