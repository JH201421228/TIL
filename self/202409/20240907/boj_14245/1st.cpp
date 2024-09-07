#include <iostream>
#include <vector>
using namespace std;


vector<int> arr;
vector<int> lazy;

void lazy_U (int s, int e, int tree_idx) {
    if (lazy[tree_idx]) {
        if (s == e) {
            arr[s] ^= lazy[tree_idx];
        }
        else {
            lazy[tree_idx*2] ^= lazy[tree_idx];
            lazy[tree_idx*2+1] ^= lazy[tree_idx];
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
        if (s == idx) {
            return arr[idx];
        }
        else {
            return 0;
        }
    }

    int mid = (s + e) / 2;
    
    return S(s, mid, tree_idx*2, idx) + S(mid+1, e, tree_idx*2+1, idx);
}

void U(int s, int e, int tree_idx, int l, int r, int val) {
    lazy_U(s, e, tree_idx);

    if (s > r || e < l) {
        return;
    }

    if (s >= l && e <= r) {
        if (s == e) {
            arr[s] ^= val;
        }
        else {
            lazy[tree_idx*2] ^= val;
            lazy[tree_idx*2+1] ^= val;
        }
        return;
    }

    int mid = (s + e) / 2;

    U(s, mid, tree_idx*2, l, r, val);
    U(mid+1, e, tree_idx*2+1, l, r, val);
}

int main () {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int N;
    cin >> N;

    arr.resize(N+1);
    lazy.resize(4*N+1);

    for (int i = 0; i < N; ++i) {
        cin >> arr[i+1];
    }

    int M;
    cin >> M;

    for (int i = 0; i < M; ++i) {
        int t;
        cin >> t;

        if (t == 1) {
            int a, b, c;
            cin >> a >> b >> c;

            U(1, N, 1, a+1, b+1, c);
        }
        else {
            int a;
            cin >> a;

            cout << S(1, N, 1, a+1) << "\n";
        }
    }

    return 0;
}