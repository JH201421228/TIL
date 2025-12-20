#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


int N, M, Q;
int arr[200'001];
int V[200'001];
int tree[800'001];
vector<int> L, R;


int I(int s, int e, int tree_idx) {
    if (s == e) {
        if (V[s]) tree[tree_idx] = arr[s];
        else tree[tree_idx] = -1e9;

        return tree[tree_idx];
    }

    int mid = (s+e) >> 1;

    return tree[tree_idx] = max(I(s, mid, tree_idx*2), I(mid+1, e, tree_idx*2+1));
}


int U(int s, int e, int idx, int tree_idx, int val) {
    if (s > idx || e < idx) return tree[tree_idx];

    if (s == e) {
        tree[tree_idx] = val;
        return val;
    }

    int mid = (s+e) >> 1;

    return tree[tree_idx] = max(U(s, mid, idx, tree_idx*2, val), U(mid+1, e, idx, tree_idx*2+1, val));
}


void solve() {
    cin >> N >> M >> Q;

    for (int idx = 0; idx < N; ++idx) cin >> arr[idx+1];
    
    for (int idx = 0; idx < M; ++idx) {
        int tmp; cin >> tmp;
        L.emplace_back(tmp);
    }

    for (int idx = 0; idx < M; ++idx) {
        int tmp; cin >> tmp;
        R.emplace_back(tmp);
    }

    sort(L.begin(), L.end(), [](auto const& a, auto const& b) {
        return a < b;
    });

    sort(R.begin(), R.end(), [](auto const& a, auto const& b) {
        return a < b;
    });

    int cur_idx = 0;
    for (int idx = 0; idx < M; ++idx) {
        if (L[idx] > R[idx]) {
            for (int i = 0; i < Q; ++i) cout << 1'000'000'000 << '\n';
            return;
        }

        int l = max(cur_idx, L[idx]);
        int r = max(cur_idx, R[idx]);

        for (int i = l; i < r+1; ++i) {
            V[i] = 1;
        }

        cur_idx = r;
    }

    I(1, N, 1);

    for (int i = 0; i < Q; ++i) {
        int x, y; cin >> x >> y;

        if (V[x]) U(1, N, x, 1, arr[y]);
        else U(1, N, x, 1, -1e9);

        if (V[y]) U(1, N, y, 1, arr[x]);
        else U(1, N, y, 1, -1e9);

        swap(arr[x], arr[y]);

        cout << tree[1] << '\n';
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